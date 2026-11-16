# singularity_oop

Учебный проект по ООП. Тут постепенно будет собираться ядро интернет-магазина.

## Что уже есть

- `src/product.py` класс `Product` (товар): название, описание, цена и количество в наличии.
- `src/category.py` класс `Category` (категория): название, описание и список товаров.
  У класса есть два общих счетчика, `category_count` и `product_count`.
  Они сами увеличиваются при создании каждой новой категории.
- `src/utils.py` загрузка категорий и товаров из JSON файла (пример лежит в `data/products.json`).
- `main.py` небольшой пример использования классов.

## Установка

```bash
poetry install
```

## Запуск

```bash
poetry run python main.py
poetry run python -m src.utils
```

## Тесты

```bash
poetry run pytest --cov=src --cov-report=html
```

Отчет о покрытии лежит в папке `htmlcov`, открыть `htmlcov/index.html`. Сейчас покрытие 92%.

## Линтеры

```bash
poetry run flake8 .
poetry run black .
poetry run isort .
poetry run mypy src
```
