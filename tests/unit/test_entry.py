# The MIT License (MIT)
#
# Copyright (c) 2024-2025 Almaz Ilaletdinov <a.ilaletdinov@yandex.ru>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
# OR OTHER DEALINGS IN THE SOFTWARE.

"""Unit test flake8-one-class plugin."""

import ast
from typing import Callable

import pytest

from flake8_one_class.entry import Plugin

_PLUGIN_RUN_T = Callable[
    [str],
    list[tuple[int, int, str]],
]


@pytest.fixture
def plugin_run() -> _PLUGIN_RUN_T:
    """Fixture for easy run plugin."""
    def _plugin_run(code: str) -> list[tuple[int, int, str]]:  # noqa: WPS430
        """Plugin run result."""
        plugin = Plugin(ast.parse(code))
        return [
            (viol[0], viol[1], viol[2])
            for viol in plugin.run()
        ]
    return _plugin_run


def test_wrong(plugin_run: _PLUGIN_RUN_T) -> None:
    """Test wrong case."""
    got = plugin_run('\n'.join([
        'class Animal(object):',
        '    pass',
        '',
        'class Animal(object):',
        '    pass',
    ]))

    assert got == [
        (
            1,
            0,
            'FOC100 found module with more than one public class',
        ),
    ]


def test_valid(plugin_run: _PLUGIN_RUN_T) -> None:
    """Test valid case."""
    got = plugin_run('\n'.join([
        'class Animal(object):',
        '    pass',
    ]))

    assert not got


def test_with_private_class(plugin_run: _PLUGIN_RUN_T) -> None:
    """Test valid case."""
    got = plugin_run('\n'.join([
        'class Animal(object):',
        '    pass',
        '',
        'class _DbRecord(object):',
        '    pass',
    ]))

    assert not got
