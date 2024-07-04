from sqlalchemy import create_engine
import pytest


@pytest.fixture
def rides_db():
    # setup
    conn = create_engine('duckdb:///../../data/bikes.ddb').connect()

    yield conn

    # teardown
    conn.close()
