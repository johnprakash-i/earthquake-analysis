from services.crud_service import execute_query


# 1. Top 10 strongest earthquakes
def top_10_strongest():
    sql = """
        SELECT *
        FROM earthquakes
        ORDER BY mag DESC
        LIMIT 10;
    """
    return execute_query(sql)


# 2. Top 10 deepest earthquakes
def top_10_deepest():
    sql = """
        SELECT *
        FROM earthquakes
        ORDER BY depth_km DESC
        LIMIT 10;
    """
    return execute_query(sql)


# 3. Shallow <50 km & strong >7.5
def shallow_strong():
    sql = """
        SELECT *
        FROM earthquakes
        WHERE depth_km < 50 AND mag > 7.5;
    """
    return execute_query(sql)


# # 4. Average depth per continent
# def avg_depth_per_continent():
#     sql = """
#         SELECT continent, ROUND(AVG(depth_km),3) AS avg_depth
#         FROM earthquakes
#         WHERE continent IS NOT NULL
#         GROUP BY continent;
#     """
#     return execute_query(sql)


# 5. Avg magnitude by magType
def avg_mag_by_type():
    sql = """
        SELECT magType, AVG(mag) AS average_magnitude
        FROM earthquakes
        GROUP BY magType;
    """
    return execute_query(sql)


# 6. Year with most earthquakes
def year_with_most_quakes():
    sql = """
        SELECT year, COUNT(*) AS total_earthquakes
        FROM earthquakes
        GROUP BY year
        ORDER BY total_earthquakes DESC
        LIMIT 1;
    """
    return execute_query(sql)


# 7. Month with highest earthquakes
def month_with_most_quakes():
    sql = """
        SELECT month, COUNT(*) AS total
        FROM earthquakes
        GROUP BY month
        ORDER BY total DESC
        LIMIT 1;
    """
    return execute_query(sql)


# 8. Day of week with most earthquakes
def day_with_most_quakes():
    sql = """
        SELECT day_of_week, COUNT(*) AS total
        FROM earthquakes
        GROUP BY day_of_week
        ORDER BY total DESC
        LIMIT 1;
    """
    return execute_query(sql)


# 9. Count earthquakes per hour
def quakes_per_hour():
    sql = """
        SELECT HOUR(time) AS hour, COUNT(*) AS earthquakes_count
        FROM earthquakes
        WHERE time IS NOT NULL
        GROUP BY hour
        ORDER BY hour;
    """
    return execute_query(sql)


# 10. Most active reporting network
def most_active_network():
    sql = """
        SELECT net, COUNT(*) AS total
        FROM earthquakes
        GROUP BY net
        ORDER BY total DESC
        LIMIT 1;
    """
    return execute_query(sql)


# 14. Reviewed vs automatic
def status_counts():
    sql = """
        SELECT status, COUNT(*) AS counts
        FROM earthquakes
        GROUP BY status;
    """
    return execute_query(sql)


# 15. Count by earthquake type
def count_by_type():
    sql = """
        SELECT type, COUNT(*) AS counts
        FROM earthquakes
        GROUP BY type;
    """
    return execute_query(sql)


# 16. Count by data types
def count_by_data_type():
    sql = """
        SELECT types, COUNT(*) AS number_of_earthquakes
        FROM earthquakes
        GROUP BY types;
    """
    return execute_query(sql)


# # 17. Avg RMS and Gap by continent
# def avg_rms_gap_by_continent():
#     sql = """
#         SELECT continent,
#                ROUND(AVG(rms),3) AS avg_rms,
#                ROUND(AVG(gap),3) AS avg_gap
#         FROM earthquakes
#         GROUP BY continent;
#     """
#     return execute_query(sql)


# 18. High station coverage
def high_station_coverage(threshold=100):
    sql = f"""
        SELECT *
        FROM earthquakes
        WHERE nst > {threshold};
    """
    return execute_query(sql)


# 19. Tsunamis per year
def tsunamis_per_year():
    sql = """
        SELECT year, COUNT(*) AS tsunami_counts
        FROM earthquakes
        WHERE tsunamis = 1
        GROUP BY year
        ORDER BY year;
    """
    return execute_query(sql)


# # 20. Count earthquakes by alert levels
# def quakes_by_alert_level():
#     sql = """
#         SELECT alert, COUNT(*) AS total
#         FROM earthquakes
#         WHERE alert IS NOT NULL
#         GROUP BY alert;
#     """
#     return execute_query(sql)


# 21. Top 5 avg magnitude (last 10 years)
def top_countries_avg_mag_10yr():
    sql = """
        SELECT country, AVG(mag) AS average
        FROM earthquakes
        WHERE year >= YEAR(CURDATE()) - 10
        GROUP BY country
        ORDER BY average DESC
        LIMIT 5;
    """
    return execute_query(sql)


# 22. Countries with both shallow & deep in same month
def shallow_deep_same_month():
    sql = """
        SELECT country, year, month
        FROM earthquakes
        WHERE depth_type IN ('shallow','deep')
        GROUP BY country, year, month
        HAVING SUM(CASE WHEN depth_type = 'shallow' THEN 1 ELSE 0 END) > 0
           AND SUM(CASE WHEN depth_type = 'deep' THEN 1 ELSE 0 END) > 0;
    """
    return execute_query(sql)


# 23. Year-over-year growth
def yoy_growth():
    sql = """
        WITH yearly_counts AS (
            SELECT year, COUNT(*) AS total_quakes
            FROM earthquakes
            GROUP BY year
        ),
        growth AS (
            SELECT year, total_quakes,
                   LAG(total_quakes) OVER (ORDER BY year) AS previous_year_quakes
            FROM yearly_counts
        )
        SELECT year, total_quakes, previous_year_quakes,
               ROUND(((total_quakes - previous_year_quakes) / previous_year_quakes) * 100, 2) AS yoy_growth_percentage
        FROM growth
        WHERE previous_year_quakes IS NOT NULL;
    """
    return execute_query(sql)


# 24. Top 3 active regions
def top_active_regions():
    sql = """
        SELECT country,
               COUNT(*) AS frequency,
               ROUND(AVG(mag),3) AS avg_mag,
               ROUND(COUNT(*) * AVG(mag),3) AS activity_score
        FROM earthquakes
        GROUP BY country
        ORDER BY activity_score DESC
        LIMIT 3;
    """
    return execute_query(sql)


# 25. Avg depth within ±5° of equator
def avg_depth_equator():
    sql = """
        SELECT country,
               COUNT(*) AS total,
               ROUND(AVG(depth_km),3) AS avg_depth
        FROM earthquakes
        WHERE latitude BETWEEN -5 AND 5
        GROUP BY country
        ORDER BY avg_depth DESC;
    """
    return execute_query(sql)


# 26. Highest shallow/deep ratio
def shallow_deep_ratio():
    sql = """
        SELECT country,
               SUM(CASE WHEN depth_type='shallow' THEN 1 END) AS shallow_count,
               SUM(CASE WHEN depth_type='deep' THEN 1 END) AS deep_count,
               SUM(CASE WHEN depth_type='shallow' THEN 1 END) /
               NULLIF(SUM(CASE WHEN depth_type='deep' THEN 1 END), 0) AS ratio
        FROM earthquakes
        GROUP BY country
        ORDER BY ratio DESC;
    """
    return execute_query(sql)


# 27. Magnitude difference (tsunami vs non-tsunami)
def mag_diff_tsunami():
    sql = """
        SELECT
            AVG(CASE WHEN tsunami = 1 THEN mag END) AS avg_tsunami,
            AVG(CASE WHEN tsunami = 0 THEN mag END) AS avg_non_tsunami,
            AVG(CASE WHEN tsunami = 1 THEN mag END) -
            AVG(CASE WHEN tsunami = 0 THEN mag END) AS difference
        FROM earthquakes;
    """
    return execute_query(sql)


# 28. Lowest reliability (gap + rms)
def lowest_reliability():
    sql = """
        SELECT id, time, place, gap, rms,
               (COALESCE(gap,0)+COALESCE(rms,0))/2 AS error_score
        FROM earthquakes
        ORDER BY error_score DESC
        LIMIT 50;
    """
    return execute_query(sql)


# 29. Consecutive quakes within 50 km & 1 hour
def consecutive_quakes():
    sql = """
 WITH ordered AS (
  SELECT
    id,
    time,
    latitude,
    longitude,
    LAG(id)        OVER (ORDER BY time) AS prev_id,
    LAG(time)      OVER (ORDER BY time) AS prev_time,
    LAG(latitude)  OVER (ORDER BY time) AS prev_lat,
    LAG(longitude) OVER (ORDER BY time) AS prev_lon
  FROM earthquakes
)
SELECT
  id,
  prev_id,
  time,
  prev_time,
  TIMESTAMPDIFF(MINUTE, prev_time, time) AS minutes_between,
  haversine.distance_km
FROM ordered
CROSS JOIN LATERAL (
    SELECT 
      6371 * 2 * ASIN(
        SQRT(
          POWER(SIN(RADIANS((latitude - prev_lat) / 2)), 2) +
          COS(RADIANS(prev_lat)) * COS(RADIANS(latitude)) *
          POWER(SIN(RADIANS((longitude - prev_lon) / 2)), 2)
        )
      ) AS distance_km
) AS haversine
WHERE prev_id IS NOT NULL
  AND TIMESTAMPDIFF(MINUTE, prev_time, time) <= 60
  AND haversine.distance_km <= 50
ORDER BY time;

    """
    return execute_query(sql)


# 30. Highest frequency deep-focus (>300km)
def deep_focus_regions():
    sql = """
        SELECT country, COUNT(*) AS deep_count
        FROM earthquakes
        WHERE depth_km > 300 and country is not null
        GROUP BY country
        ORDER BY deep_count DESC
        LIMIT 10;
    """
    return execute_query(sql)
