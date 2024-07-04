import numpy as np
import pandas as pd

import geo


def test_load_gpx():
    df = geo.load_gpx('hike.gpx')
    assert len(df) == 358

    types = pd.Series([np.float64] * 3, index=['lat', 'lng', 'height'])
    pd.testing.assert_series_equal(df.dtypes, types)


def test_total_distance():
    df = geo.load_gpx('hike.gpx')
    dist = geo.total_distance(df)
    np.testing.assert_almost_equal(dist, 8.667, decimal=3)
