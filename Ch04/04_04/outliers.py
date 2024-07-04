import pandas as pd


def outliers(data: pd.Series, tolerance=2) -> pd.Series:
    """Find outliers in data

    >>> s = pd.Series([1, 0, 1, 6, 1, 1])
    >>> outliers(s)
    3    6
    dtype: int64
    """
    if len(data) == 0:
        raise ValueError('empty data')
    if tolerance <= 0:
        raise ValueError(f'tolerance ({tolerance!r}) must be > 0')

    z_score = (data - data.mean()) / data.std()
    return data[z_score.abs() > tolerance]
