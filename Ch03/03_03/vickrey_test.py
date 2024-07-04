import pandas as pd
import pytest

import vickrey

test_cases = [
    # values, expected, err
    (pd.Series([3, 1, 2]), 2, False),
    (pd.Series([3, 3, 3]), 3, False),
    pytest.param(pd.Series([]), 0, True, id='empty'),
]

@pytest.mark.parametrize('values, expected, err', test_cases)
def test_second_largest(values, expected, err):
    if err:
        with pytest.raises(ValueError):
            vickrey.second_largest(values)
        return

    assert vickrey.second_largest(values) == expected
