# run_tests.py
import unittest
from unitest import TestDataService

if __name__ == '__main__':
    # Создание тестового набора
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestDataService)

    # Запуск тестов
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)

    # Вывод статистики
    print(f"\n{'='*50}")
    print(f"Тестов выполнено: {result.testsRun}")
    print(f"Успешно: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Провалено: {len(result.failures)}")
    print(f"Ошибок: {len(result.errors)}")
    print('='*50)
