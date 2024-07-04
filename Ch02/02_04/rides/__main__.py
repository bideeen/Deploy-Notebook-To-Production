from argparse import ArgumentParser
from pathlib import Path

import rides

if __name__ == '__main__':
    parser = ArgumentParser(description='Analyze bike rides')
    parser.add_argument('db_file', help='Path to DuckDB database file')
    args = parser.parse_args()

    if not Path(args.db_file).exists():
        print(f'error: {args.db_file!r} is not a file')
        raise SystemExit(1)

    df = rides.load_rides(args.db_file)
    df = rides.clean_rides(df)
    bike_id, duration = rides.bike_with_most_time(df)
    print(f'{bike_id}: {duration}min')
