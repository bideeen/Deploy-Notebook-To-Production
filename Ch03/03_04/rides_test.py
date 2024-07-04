import pandas as pd

import rides


def test_load(rides_db):
    start_time = pd.Timestamp('2017-01-01')
    end_time = pd.Timestamp('2017-07-01')
    df = rides.load_rides(rides_db, start_time, end_time)
    assert len(df) == 108226
