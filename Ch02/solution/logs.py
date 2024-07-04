from sqlalchemy import create_engine
import pandas as pd
from matplotlib.axes import Axes


def load(db_file: str) -> pd.DataFrame:
    """Load logs from DuckDB database file."""
    conn = create_engine('duckdb:///' + db_file)
    return pd.read_sql('SELECT * FROM logs', conn)


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Clean invalid values and normalize levels."""
    mask = (
        (df['message'] == '') |
        (df['time'] < pd.Timestamp('2024-04', tz='UTC'))
    )
    df = df[~mask].copy()

    # info -> INFO
    df.loc[df['level'] == 'info', 'level'] = 'INFO'
    return df


def plot_level_counts(df: pd.DataFrame) -> Axes:
    """Return chart of count by level."""
    return df.groupby('level').count()['time'].plot.bar()