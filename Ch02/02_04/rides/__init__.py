import numpy as np
import pandas as pd

from .db import load_rides


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
