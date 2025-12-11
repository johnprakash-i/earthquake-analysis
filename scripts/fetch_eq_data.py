import requests
import pandas as pd
from datetime import datetime, timedelta
import calendar
import re

BASE = "https://earthquake.usgs.gov/fdsnws/event/1/query"


def month_ranges(start_year, start_month, end_year, end_month):
    y, m = start_year, start_month
    while (y < end_year) or (y == end_year and m <= end_month):
        first = datetime(y, m, 1)
        last_day = calendar.monthrange(y, m)[1]
        last = datetime(y, m, last_day, 23, 59, 59)
        yield first, last
        if m == 12:
            y += 1
            m = 1
        else:
            m += 1


def fetch_for_range(start_dt, end_dt, minmag, timeout=60):
    params = {
        "format": "geojson",
        "starttime": start_dt.strftime("%Y-%m-%dT%H:%M:%S"),
        "endtime": end_dt.strftime("%Y-%m-%dT%H:%M:%S"),
        "minmagnitude": float(minmag),
    }
    r = requests.get(BASE, params=params, timeout=timeout)
    r.raise_for_status()
    return r.json()


def parse_feature(f):
    p = f.get("properties", {})
    g = f.get("geometry", {}) or {}
    coords = g.get("coordinates", [None, None, None])
    record = {
        "id": f.get("id"),
        "time": (
            pd.to_datetime(p.get("time"), unit="ms", utc=True)
            if p.get("time")
            else None
        ),
        "updated": (
            pd.to_datetime(p.get("updated"), unit="ms", utc=True)
            if p.get("updated")
            else None
        ),
        "latitude": coords[1],
        "longitude": coords[0],
        "depth_km": coords[2],
        "mag": p.get("mag"),
        "magType": p.get("magType"),
        "place": p.get("place"),
        "status": p.get("status"),
        "tsunami": p.get("tsunami"),
        "sig": p.get("sig"),
        "net": p.get("net"),
        "nst": p.get("nst"),
        "dmin": p.get("dmin"),
        "rms": p.get("rms"),
        "gap": p.get("gap"),
        "magError": p.get("magError"),
        "depthError": p.get("depthError"),
        "magNst": p.get("magNst"),
        "locationSource": p.get("locationSource"),
        "magSource": p.get("magSource"),
        "types": p.get("types"),
        "ids": p.get("ids"),
        "sources": p.get("sources"),
        "type": p.get("type"),
    }
    return record


def collect(start_year, start_month, end_year, end_month, minmag):
    rows = []
    for s, e in month_ranges(start_year, start_month, end_year, end_month):
        try:
            js = fetch_for_range(s, e, minmag=minmag)
        except requests.HTTPError as exc:
            print("HTTP error for", s, e, exc)

            continue
        features = js.get("features", [])
        for f in features:
            rows.append(parse_feature(f))
        print(f"Fetched {len(features)} events for {s.strftime('%Y-%m')}")

    df = pd.DataFrame(rows)
    return df


if __name__ == "__main__":
    end = datetime.utcnow()
    start = end.replace(year=end.year - 5)
    df = collect(start.year, start.month, end.year, end.month, minmag=4)
    print(df.shape)
    df.to_csv("../data/earthquakes_raw.csv", index=False)
