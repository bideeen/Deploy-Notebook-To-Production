from pathlib import Path
from subprocess import run
import sys

root_dir = Path(__file__).parent.absolute()


def test_nb(tmp_path):
    nb_file = root_dir / 'rides.ipynb'
    out_file = tmp_path / 'rides.html'

    cmd = [
        sys.executable,
        '-m', 'nbconvert',
        '--execute',
        '--to', 'html',
        '--output', str(out_file),
        str(nb_file),
    ]
    out = run(cmd)
    assert out.returncode == 0
