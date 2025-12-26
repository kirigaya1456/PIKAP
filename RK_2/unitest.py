# test_program_service.py
import unittest
from main import Program, Computer, ProgramComputer, DataService


class TestDataService(unittest.TestCase):
    def setUp(self):
        """Настройка тестовых данных перед каждым тестом"""
        self.computers = [
            Computer(1, 'Рабочая станция инженера'),
            Computer(2, 'Сервер базы данных'),
            Computer(3, 'Ноутбук руководителя'),
            Computer(11, 'АРМ бухгалтера'),
            Computer(22, 'Аналитическая станция'),
            Computer(33, 'Антивирусный сервер'),
        ]

        self.programs = [
            Program(1, 'AutoCAD', 2500, 1),
            Program(2, '1С:Бухгалтерия', 1500, 2),
            Program(3, 'Microsoft Office', 3000, 3),
            Program(4, 'Adobe Photoshop', 5000, 3),
            Program(5, 'Visual Studio Code', 500, 3),
            Program(6, 'Антивирус Касперского', 800, 11),
            Program(7, '7-Zip', 50, 22),
        ]

        self.programs_computers = [
            ProgramComputer(1, 1),
            ProgramComputer(2, 2),
            ProgramComputer(3, 3),
            ProgramComputer(3, 4),
            ProgramComputer(3, 5),
            ProgramComputer(11, 1),
            ProgramComputer(11, 6),
            ProgramComputer(22, 2),
            ProgramComputer(22, 7),
            ProgramComputer(33, 3),
            ProgramComputer(33, 4),
            ProgramComputer(33, 5),
        ]

        self.service = DataService(self.computers, self.programs, self.programs_computers)

    def test_get_programs_ending_with_e(self):
        """Тест 1: Поиск программ, заканчивающихся на 'e'"""
        # Act
        result = self.service.get_programs_ending_with_e()

        # Assert
        # Проверяем, что все найденные программы заканчиваются на 'e'
        for program_name, _ in result:
            self.assertTrue(program_name.endswith('e'),
                          f"Программа '{program_name}' должна заканчиваться на 'e'")

        # Проверяем конкретные ожидаемые результаты
        expected_programs = ['Visual Studio Code', 'Microsoft Office']
        result_programs = [name for name, _ in result]

        self.assertIn('Visual Studio Code', result_programs)
        self.assertIn('Microsoft Office', result_programs)
        self.assertEqual(len(result_programs), len(expected_programs))

        # Проверяем, что программы связаны с правильными компьютерами
        result_dict = dict(result)
        self.assertEqual(result_dict['Visual Studio Code'], 'Ноутбук руководителя')
        self.assertEqual(result_dict['Microsoft Office'], 'Ноутбук руководителя')

    def test_get_avg_program_size_per_computer(self):
        """Тест 2: Расчет среднего размера программ на компьютере"""
        # Act
        result = self.service.get_avg_program_size_per_computer()

        # Assert
        # Проверяем структуру результата
        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(item, tuple) and len(item) == 2 for item in result))

        # Проверяем сортировку по возрастанию среднего размера
        sizes = [size for _, size in result]
        self.assertEqual(sizes, sorted(sizes))

        # Проверяем конкретные вычисления
        result_dict = dict(result)

        # Для "Ноутбук руководителя" должны быть 3 программы: 3000, 5000, 500
        # Среднее: (3000 + 5000 + 500) / 3 = 2833.33
        expected_avg = round((3000 + 5000 + 500) / 3, 2)
        self.assertAlmostEqual(result_dict['Ноутбук руководителя'], expected_avg, places=2)

        # Для "Аналитическая станция" должны быть 2 программы: 1500, 50
        # Среднее: (1500 + 50) / 2 = 775
        self.assertEqual(result_dict['Аналитическая станция'], 50.0)

        # Проверяем, что компьютеры без программ не включены в результат
        computer_names = [name for name, _ in result]
        self.assertNotIn('Антивирусный сервер', computer_names)  # Только связи многие-ко-многим

    def test_get_a_computers_with_programs(self):
        """Тест 3: Поиск компьютеров на букву 'А' с программами"""
        # Act
        result = self.service.get_a_computers_with_programs()

        # Assert
        # Проверяем, что все компьютеры начинаются с 'А'
        computer_names = {name for name, _ in result}
        for name in computer_names:
            self.assertTrue(name.startswith('А'),
                          f"Компьютер '{name}' должен начинаться с 'А'")

        # Проверяем конкретные ожидаемые компьютеры
        expected_computers = ['АРМ бухгалтера', 'Аналитическая станция', 'Антивирусный сервер']
        self.assertEqual(set(computer_names), set(expected_computers))

        # Проверяем программы для конкретных компьютеров
        programs_by_computer = {}
        for computer, program in result:
            if computer not in programs_by_computer:
                programs_by_computer[computer] = []
            programs_by_computer[computer].append(program)

        # АРМ бухгалтера должен иметь AutoCAD и Антивирус Касперского
        self.assertIn('AutoCAD', programs_by_computer['АРМ бухгалтера'])
        self.assertIn('Антивирус Касперского', programs_by_computer['АРМ бухгалтера'])

        # Аналитическая станция должна иметь 1С:Бухгалтерия и 7-Zip
        self.assertIn('1С:Бухгалтерия', programs_by_computer['Аналитическая станция'])
        self.assertIn('7-Zip', programs_by_computer['Аналитическая станция'])

        # Антивирусный сервер должен иметь Microsoft Office, Adobe Photoshop, Visual Studio Code
        self.assertIn('Microsoft Office', programs_by_computer['Антивирусный сервер'])
        self.assertIn('Adobe Photoshop', programs_by_computer['Антивирусный сервер'])
        self.assertIn('Visual Studio Code', programs_by_computer['Антивирусный сервер'])


if __name__ == '__main__':
    unittest.main()
