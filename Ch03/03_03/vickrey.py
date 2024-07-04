import pandas as pd


def second_largest(values: pd.Series):
    """Return second largest value in values."""
    if len(values) < 2:
        raise ValueError('must have at least two values')

    return values.sort_values().iloc[-2]
