import streamlit as st
import pandas as pd
from services import analytical_service as a

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Earthquake Analytics Dashboard", layout="wide", page_icon="🌍"
)

# ---------- HEADER ----------
st.markdown(
    """
# 🌍 Earthquake Analytics Dashboard  
Gain deep insights from global earthquake activity using database-powered analytical queries.
"""
)

# Divider
st.markdown("---")

# ---------- SIDEBAR INFO ----------
with st.sidebar:
    st.header("📌 About This App")
    st.write(
        """
    This dashboard helps you explore:
    - 🔥 Strongest & deepest earthquakes  
    - 🌋 Tsunami-linked quakes  
    - 🕒 Time-based analytics  
    - 🌎 Country & region insights  
    - 🛰 Station + network reliability  
    """
    )

    st.info(
        "Select a query from the dropdown in the main screen and click **Run Analysis**."
    )

# ---------- MAIN QUERY MAPPING ----------
queries = {
    "Top 10 strongest earthquakes": a.top_10_strongest,
    "Top 10 deepest earthquakes": a.top_10_deepest,
    "Shallow earthquakes <50km & mag >7.5": a.shallow_strong,
    "Average magnitude per magType": a.avg_mag_by_type,
    "Year with most earthquakes": a.year_with_most_quakes,
    "Month with highest earthquakes": a.month_with_most_quakes,
    "Day with most earthquakes": a.day_with_most_quakes,
    "Earthquakes per hour": a.quakes_per_hour,
    "Most active reporting network": a.most_active_network,
    "Reviewed vs automatic": a.status_counts,
    "Count by earthquake type": a.count_by_type,
    "Count by data type": a.count_by_data_type,
    "Events with high station coverage": a.high_station_coverage,
    "Tsunamis per year": a.tsunamis_per_year,
    "Top avg mag countries (10yr)": a.top_countries_avg_mag_10yr,
    "Countries with shallow & deep same month": a.shallow_deep_same_month,
    "Year-over-year growth": a.yoy_growth,
    "Top 3 active regions": a.top_active_regions,
    "Avg depth near equator": a.avg_depth_equator,
    "Shallow/Deep ratio": a.shallow_deep_ratio,
    "Magnitude diff (tsunami vs none)": a.mag_diff_tsunami,
    "Lowest data reliability": a.lowest_reliability,
    "Consecutive quakes (50km & 1hr)": a.consecutive_quakes,
    "Deep-focus regions": a.deep_focus_regions,
}

# ---------- UI ELEMENTS ----------
st.markdown("### 🔍 Select an analysis to run")
selected = st.selectbox("", list(queries.keys()))

# Add spacing
st.markdown("")

# ---------- RUN BUTTON ----------
if st.button("🚀 Run Analysis", use_container_width=True):
    st.markdown("### 📊 Results")
    st.markdown(f"**Selected Query:** `{selected}`")

    df = queries[selected]()

    if df is None or len(df) == 0:
        st.warning("⚠️ No data returned for this query.")
    else:
        st.dataframe(df, use_container_width=True)

        # Auto chart for numeric analysis
        numeric = df.select_dtypes(include=["float", "int"])
        if not numeric.empty and df.shape[0] > 1:
            st.markdown("### 📈 Trend Visualization")
            st.line_chart(numeric)

st.markdown("---")
st.caption("© 2025 Earthquake Analytics — Developed by John Prakash")
