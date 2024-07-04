import pandas as pd
import pytest
import yaml

import tags


def load_tags_cases():
    with open('tags_cases.yml') as fp:
        for case in yaml.safe_load(fp):
            input = pd.Series(case['tags'])
            expected = pd.Series(case['expected'])
            param = (input, expected)
            if (name := case.get('name')):
                param = pytest.param(*param, id=name)
            yield param


@pytest.mark.parametrize('input, expected', load_tags_cases())
def test_tags(input, expected):
    result = tags.clean_tags(input)
    pd.testing.assert_series_equal(result, expected)
