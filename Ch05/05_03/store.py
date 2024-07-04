import pandas as pd


def load_data(file_name):
    return pd.read_parquet(file_name)


def total_by_sku(df):
    by_sku = {}
    for _, row in df.iterrows():
        sku = row['sku']
        by_sku[sku] = by_sku.get(sku, 0.0) + row['amount'] * row['price']

    return by_sku


def gen_report(by_sku, out_file):
    df = pd.DataFrame.from_dict(
            by_sku,
            orient='index',
            columns=['revenue'],
    )
    df = df.reset_index(names='sku')
    with open(out_file, 'w') as out:
        df.to_csv(out, index=False)


def gen_sku_report(file_name, month, out_file):
    df = load_data(file_name)
    df = df[df['time'].dt.strftime('%Y-%m') == month]

    by_sku = total_by_sku(df)
    gen_report(by_sku, out_file)
