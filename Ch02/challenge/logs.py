from sqlalchemy import create_engine
import pandas as pd
from matplotlib.axes import Axes


def load(dbfile: str) -> pd.DataFrame:
    """Load logs from DuckDB database file."""
    with create_engine('duckdb:///' + dbfile).connect() as conn:
        return pd.read_sql('select * from logs', conn)


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Load logs from DuckDB database file. """
    mask = (
        (df['message'] == '') |
        (df['time'] < pd.Timestamp('2024-04', tz='UTC'))
    )
    print('size:', len(df))
    df = df[~mask].copy()

    # info -> INFO
    df.loc[df['level'] == 'info', 'level'] = 'INFO'
    return df


def plot_level_counts(df: pd.DataFrame) -> Axes:
    """Return chart of count by level."""
    return df.groupby('level').count()['time'].plot.bar()
