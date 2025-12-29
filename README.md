<!---
SPDX-FileCopyrightText: Copyright (c) 2024-2026 Almaz Ilaletdinov <a.ilaletdinov@yandex.ru>
SPDX-License-Identifier: MIT
--->

# flake8-one-class

[![test](https://github.com/blablatdinov/flake8-one-class/actions/workflows/test.yml/badge.svg)](https://github.com/blablatdinov/flake8-one-class/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/blablatdinov/flake8-one-class/branch/master/graph/badge.svg)](https://codecov.io/gh/blablatdinov/flake8-one-class)
[![Python Version](https://img.shields.io/pypi/pyversions/flake8-one-class.svg)](https://pypi.org/project/flake8-one-class/)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

## Background

In Python modules, having multiple classes in a single file can often indicate overly complex code or an unclear separation of concerns. The flake8-one-class plugin enforces a single public class per module to encourage modular and maintainable code design. Private (internal) classes are allowed but are intended for module-level encapsulation only.

## Installation

Install flake8-one-class using pip:

```
pip install flake8-one-class
```

## Usage

After installation, flake8-one-class will automatically run with flake8:

```
flake8 your_project_directory
```

This plugin checks each module for multiple public class definitions. If more than one public class is detected, an error is raised.

## Example

Given the following Python code:

```python
class Animal:
    pass

class Plant:
    pass
```

Running flake8 will produce the following error:

```
your_file.py:1:1: FOC100 found module with more than one public class
```

Using only one public class in the module will resolve the error:

```python
class Animal:
    pass

class _Helper:  # private class is allowed
    pass
```


## License

[MIT](https://github.com/blablatdinov/flake8-one-class/blob/master/LICENSE)


## Credits

This project was generated with [`wemake-python-package`](https://github.com/wemake-services/wemake-python-package). Current template version is: [9899cb192f754a566da703614227e6d63227b933](https://github.com/wemake-services/wemake-python-package/tree/9899cb192f754a566da703614227e6d63227b933). See what is [updated](https://github.com/wemake-services/wemake-python-package/compare/9899cb192f754a566da703614227e6d63227b933...master) since then.
