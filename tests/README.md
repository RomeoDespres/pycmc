# Tests

This directory setup uses the `py.test` framework without setuptools/installing
your package prior to execution of the test runner.

Rather, it separates the tests from module code and allows pytest to do its
magic using monkeypatching for the PYTHONPATH at each run of the tests. This
also allows for universal absolute imports, in good PEP style.

### `imports`

```
from module_name.filename import functionname
```
Where `filename` is the name of your `.py` file containing `functionname`.

### `conftest.py` - `py.test` configuration

Add your configuration as needed in this file.
