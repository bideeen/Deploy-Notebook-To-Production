import pytest
import pandas as pd

import outliers


outlier_cases = [
    # data, threshold, output, err
    pytest.param(pd.Series([]), 2, None, True, id='empty'),
    pytest.param(pd.Series([1, 2, 3]), -2, None, True, id='bad threshold'),
    pytest.param(
        pd.Series([1, 0, 1, 6, 1, 1]),
        2,
        pd.Series([6], index=[3]),
        False,
        id='normal',
    ),
]

@pytest.mark.parametrize('data, threshold, output, err', outlier_cases)
def test_outliers(data, threshold, output, err):
    if err:
        with pytest.raises(ValueError):
            outliers.outliers(data, threshold)
        return

    out = outliers.outliers(data, threshold)
    pd.testing.assert_series_equal(out, output)
