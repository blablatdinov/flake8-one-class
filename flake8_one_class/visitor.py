# SPDX-FileCopyrightText: Copyright (c) 2024-2026 Almaz Ilaletdinov <a.ilaletdinov@yandex.ru>
# SPDX-License-Identifier: MIT

"""Class visitor for checking class count in module."""

import ast
from typing import final


@final
class ModuleVisitor(ast.NodeVisitor):
    """Class visitor for checking class count in module."""

    def __init__(self) -> None:
        """Ctor."""
        self.problems: list[int] = []

    def visit_Module(self, node: ast.Module) -> None:  # noqa: N802, WPS231, C901. Flake8 plugin API
        """Visit by modules."""
        classes_count = 0
        for elem in node.body:
            if isinstance(elem, ast.ClassDef) and not elem.name.startswith('_'):
                classes_count += 1
            if classes_count > 1:
                self.problems.append(1)
        self.generic_visit(node)
