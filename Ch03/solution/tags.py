import pandas as pd


def clean_tags(tags: pd.Series) -> pd.Series:
    """Clean tags by removing whitespace and normalizing case."""
    tags = tags.str.strip()
    mask = (
        pd.isnull(tags) |
        (tags == '')
    )
    tags = tags[~mask]
    tags = tags.str.lower()
    return tags.reset_index(drop=True)
