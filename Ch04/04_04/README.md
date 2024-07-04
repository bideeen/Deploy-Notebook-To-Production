# outliers - Outlier detection for Python

This project provides way to detect outliers in Pandas Series.

## Example

```python
from outliers import outliers

data = pd.Series([1, 0, 1, 6, 1, 1])
print(outliers(data))
3    6
dtype: int64
```

## Installing

    python -m pip install outliers

## Hacking

Create a virtual environment for the project:

```
python -m venv .venv
./.venv/bin/python -m pip install -r dev-requirements.txt

Then run the tests:

```
python -m pytest -v
```
