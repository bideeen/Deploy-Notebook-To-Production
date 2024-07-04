import pandas as pd
from sqlalchemy import Engine

query_sql = '''
SELECT
    trip_id,
    bikeid AS bike_id,
    subscriber_type,
    start_time,
    duration_minutes,
    start_station_id,
    end_station_id,
FROM
    rides
WHERE
    start_time >= ?
    AND start_time < ?
'''


def load_rides(conn, start_time, end_time):
    """Load rides loads rides from in time range."""
    return pd.read_sql(query_sql, conn, params=(start_time, end_time))
