# SPDX-FileCopyrightText: Copyright (c) 2024-2026 Almaz Ilaletdinov <a.ilaletdinov@yandex.ru>
# SPDX-License-Identifier: MIT

SHELL:=/usr/bin/env bash

.PHONY: lint
lint:
	poetry run ruff check flake8_no_private_methods tests
	poetry run mypy flake8_one_class tests/**/*.py

.PHONY: unit
unit:
	poetry run pytest

.PHONY: package
package:
	poetry check
	poetry run pip check

.PHONY: test
test: package unit

.DEFAULT:
	@cd docs && $(MAKE) $@
