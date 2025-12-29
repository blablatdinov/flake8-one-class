# SPDX-FileCopyrightText: Copyright (c) 2024-2026 Almaz Ilaletdinov <a.ilaletdinov@yandex.ru>
# SPDX-License-Identifier: MIT

"""Entrypoint."""

import ast
from collections.abc import Generator
from typing import final

from flake8_one_class.visitor import ModuleVisitor


@final
class Plugin:
    """Flake8 plugin."""

    def __init__(self, tree: ast.AST) -> None:
        """Ctor."""
        self._tree = tree

    def run(self) -> Generator[tuple[int, int, str, type], None, None]:
        """Entry."""
        visitor = ModuleVisitor()
        visitor.visit(self._tree)
        for _ in visitor.problems:  # noqa: WPS526
            yield (1, 0, 'FOC100 found module with more than one public class', type(self))
