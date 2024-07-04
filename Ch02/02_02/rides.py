import numpy as np
import pandas as pd
from sqlalchemy import create_engine

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


def load_rides(db_file: str) -> pd.DataFrame:
    """Load rides loads rides from duckdb database."""
    conn = create_engine('duckdb:///' + db_file).connect()
    return pd.read_sql(query_sql, conn)


def clean_rides(df: pd.DataFrame) -> pd.DataFrame:
    """Clean rides dataframe.

    - Remove rows where duration_minutes <= 0
    - Remove row with missing bike_id
    - Remove rows with missing start_station_id or end_station_id
    """

    mask = (
        (df['duration_minutes'] > 0) &
        ~pd.isnull(df['bike_id']) &
        ~pd.isnull(df['start_station_id']) &
        ~pd.isnull(df['end_station_id'])
    )
    df = df[mask].copy()

    df['bike_id'] = df['bike_id'].astype('int64')
    df['start_station_id'] = df['start_station_id'].astype('int64')
    df['end_station_id'] = df['end_station_id'].astype('int64')

    return df


def bike_with_most_time(df: pd.DataFrame) -> tuple[np.int64, np.int64]:
    """Return bike_id and duration (in minutes) of most ridden bike."""
    row = (
        df.groupby('bike_id', as_index=False)
        ['duration_minutes'].sum()
        .iloc[-1]
    )
    return row['bike_id'], row['duration_minutes']
