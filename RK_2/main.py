# program_refactored.py
from operator import itemgetter


class Program:
    def __init__(self, id, name, size, comp_id):
        self.id = id
        self.name = name
        self.size = size  # размер в МБ
        self.comp_id = comp_id


class Computer:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class ProgramComputer:
    def __init__(self, comp_id, program_id):
        self.comp_id = comp_id
        self.program_id = program_id


class DataService:
    def __init__(self, computers, programs, programs_computers):
        self.computers = computers
        self.programs = programs
        self.programs_computers = programs_computers

    def get_one_to_many(self):
        """Создание связи один-ко-многим"""
        return [(p.name, p.size, c.name)
                for c in self.computers
                for p in self.programs
                if p.comp_id == c.id]

    def get_many_to_many(self):
        """Создание связи многие-ко-многим"""
        many_to_many_temp = [(c.name, pc.comp_id, pc.program_id)
                             for c in self.computers
                             for pc in self.programs_computers
                             if c.id == pc.comp_id]

        return [(p.name, p.size, comp_name)
                for comp_name, comp_id, program_id in many_to_many_temp
                for p in self.programs if p.id == program_id]

    def get_programs_ending_with_e(self):
        """Задание 1: программы, заканчивающиеся на 'e'"""
        one_to_many = self.get_one_to_many()
        return [(name, comp_name)
                for name, size, comp_name in one_to_many
                if name.endswith('e')]

    def get_avg_program_size_per_computer(self):
        """Задание 2: средний размер программ на компьютере"""
        one_to_many = self.get_one_to_many()
        result = []

        for c in self.computers:
            c_programs = list(filter(lambda i: i[2] == c.name, one_to_many))
            if c_programs:
                total_size = sum(size for _, size, _ in c_programs)
                avg_size = total_size / len(c_programs)
                result.append((c.name, round(avg_size, 2)))

        return sorted(result, key=itemgetter(1))

    def get_a_computers_with_programs(self):
        """Задание 3: компьютеры на 'А' с программами"""
        many_to_many = self.get_many_to_many()
        a_computers = [c for c in self.computers if c.name.startswith('А')]
        result = []

        for c in a_computers:
            c_programs = list(filter(lambda i: i[2] == c.name, many_to_many))
            c_program_names = [name for name, _, _ in c_programs]

            if c_program_names:
                for prog_name in c_program_names:
                    result.append((c.name, prog_name))
            else:
                result.append((c.name, 'Нет программ'))

        return sorted(result, key=itemgetter(0))


def print_table(headers, data):
    """Функция для форматированного вывода таблицы"""
    if not data:
        print("Нет данных для отображения")
        print()
        return

    col_widths = []
    for i in range(len(headers)):
        col_width = max(len(str(headers[i])),
                        max(len(str(row[i])) for row in data) if data else 0)
        col_widths.append(col_width)

    header_row = "  ".join(f"{headers[i]:<{col_widths[i]}}" for i in range(len(headers)))
    print(header_row)

    separator = "  ".join("-" * col_widths[i] for i in range(len(headers)))
    print(separator)

    for row in data:
        data_row = "  ".join(f"{str(row[i]):<{col_widths[i]}}" for i in range(len(row)))
        print(data_row)
    print()


def main():
    # Данные
    computers = [
        Computer(1, 'Рабочая станция инженера'),
        Computer(2, 'Сервер базы данных'),
        Computer(3, 'Ноутбук руководителя'),
        Computer(11, 'АРМ бухгалтера'),
        Computer(22, 'Аналитическая станция'),
        Computer(33, 'Антивирусный сервер'),
    ]

    programs = [
        Program(1, 'AutoCAD', 2500, 1),
        Program(2, '1С:Бухгалтерия', 1500, 2),
        Program(3, 'Microsoft Office', 3000, 3),
        Program(4, 'Adobe Photoshop', 5000, 3),
        Program(5, 'Visual Studio Code', 500, 3),
        Program(6, 'Антивирус Касперского', 800, 11),
        Program(7, '7-Zip', 50, 22),
    ]

    programs_computers = [
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

    # Создание сервиса
    service = DataService(computers, programs, programs_computers)

    # Выполнение заданий
    print('Задание 1')
    res_1 = service.get_programs_ending_with_e()
    print_table(['Программа', 'Компьютер'], res_1)

    print('Задание 2')
    res_2 = service.get_avg_program_size_per_computer()
    print_table(['Компьютер', 'Средний размер программ (МБ)'], res_2)

    print('Задание 3')
    res_3 = service.get_a_computers_with_programs()
    print_table(['Компьютер', 'Программа'], res_3)


if __name__ == '__main__':
    main()
