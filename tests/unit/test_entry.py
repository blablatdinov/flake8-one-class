# SPDX-FileCopyrightText: Copyright (c) 2024-2026 Almaz Ilaletdinov <a.ilaletdinov@yandex.ru>
# SPDX-License-Identifier: MIT

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
