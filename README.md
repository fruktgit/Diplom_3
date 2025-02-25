

## Запуск тестов
Запустить все тесты:
```sh
pytest tests --alluredir=allure_results
```

Запустить конкретный тест:
```sh
pytest tests/test_create_user.py
```

Запуск тестов с определенным маркером (например, `login`):
```sh
pytest -m "login"
```

## Просмотр отчётов
Для просмотра отчётов используется **Allure Report**:
```sh
allure serve allure_results
```
Allure позволяет визуализировать результаты тестов с подробной информацией о каждом тест-кейсе.
