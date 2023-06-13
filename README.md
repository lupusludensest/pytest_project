Запуск тестов модуля

pytest -k "test_00"
Запуск тестов из директории

pytest testing/
Запуск тестов, удовлетворяющих ключевому выражению

pytest -k "MyClass and not method"