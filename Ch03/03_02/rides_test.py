from subprocess import run
import sys


def test_nb(tmp_path):
    out_file = tmp_path / 'rides.html'

    cmd = [
        sys.executable,
        '-m', 'nbconvert',
        '--execute',
        '--to', 'html',
        '--output', str(out_file),
        'rides.ipynb',
    ]
    out = run(cmd)
    assert out.returncode == 0
