from sqlalchemy import create_engine
import pandas as pd

query_sql = '''
SELECT
    r.trip_id,
    r.bikeid AS bike_id,
    r.subscriber_type,
    r.checkout_time,
    r.duration_minutes,
    r.start_station_id,
    r.start_station_name,
    s.latitude AS start_latutide,
    s.longitude AS start_longitude,
    r.end_station_id,
    e.latitude AS end_latutide,
    e.longitude AS end_longitude
FROM 
    rides r 
        LEFT JOIN stations s ON r.start_station_id == s.station_id
        LEFT JOIN stations e ON r.end_station_id == e.station_id
;
'''

# ok


def load_rides(db_file: str) -> pd.DataFrame:
    """Load rides loads rides from duckdb database."""
    conn = create_engine('duckdb:///' + db_file).connect()
    return pd.read_sql(query_sql, conn)
