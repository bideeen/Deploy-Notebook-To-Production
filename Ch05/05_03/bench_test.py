import store


def test_bench_gen_sku_report(benchmark, tmp_path):
    out_file = tmp_path / 'by_sku.csv'
    benchmark(store.gen_sku_report, 'store.parquet', '2020-01', out_file)
