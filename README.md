# Проект онлайн магазина

## В проекте имеется один модуль class_models.py который содержит два класса:
1. Product - Класс продуктов
2. Category - Класс категорий

На модуль class_models.py написаны тесты, модули проверены линтерами:
flake8, mypy, black и isort

Ниже представлены основные зависимости:

[tool.poetry]
name = "online-store"
version = "0.1.0"
description = ""
authors = ["старченко дмитрий <starchenko.dmitr@mail.ru>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.13"


[tool.poetry.group.lint.dependencies]
flake8 = "^7.3.0"
mypy = "^1.17.1"
black = "^25.1.0"
isort = "^6.0.1"


[tool.poetry.group.dev.dependencies]
pytest = "^8.4.2"
pytest-cov = "^6.2.1"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"