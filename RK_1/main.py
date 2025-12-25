from operator import itemgetter


# класс Программа
class Program:
    def __init__(self, id, name, size, comp_id):
        self.id = id
        self.name = name
        self.size = size  # размер в МБ
        self.comp_id = comp_id


# класс Компьютер
class Computer:
    def __init__(self, id, name):
        self.id = id
        self.name = name


# класс для связи многие ко многим
class ProgramComputer:
    def __init__(self, comp_id, program_id):
        self.comp_id = comp_id
        self.program_id = program_id


# Компьютеры
computers = [
    Computer(1, 'Рабочая станция инженера'),
    Computer(2, 'Сервер базы данных'),
    Computer(3, 'Ноутбук руководителя'),
    Computer(11, 'АРМ бухгалтера'),
    Computer(22, 'Аналитическая станция'),
    Computer(33, 'Антивирусный сервер'),
]

# Программы
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


# функция для вывода результатов
def print_table(headers, data):
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
    # Связь один-ко-многим
    one_to_many = [(p.name, p.size, c.name)
                   for c in computers
                   for p in programs
                   if p.comp_id == c.id]

    # Временная связь для многие-ко-многим
    many_to_many_temp = [(c.name, pc.comp_id, pc.program_id)
                         for c in computers
                         for pc in programs_computers
                         if c.id == pc.comp_id]

    # Связь многие-ко-многим
    many_to_many = [(p.name, p.size, comp_name)
                    for comp_name, comp_id, program_id in many_to_many_temp
                    for p in programs if p.id == program_id]

    print('Задание 1')
    print('Список всех программ, у которых название заканчивается на "e", и названия компьютеров, на которых они установлены')
    # Находим программы, названия которых заканчиваются на "ов" (русская "в")
    res_1 = [(name, comp_name) for name, size, comp_name in one_to_many if name.endswith('e')]
    headers_1 = ['Программа', 'Компьютер']
    print_table(headers_1, res_1)

    print('Задание 2')
    print('Список компьютеров со средним размером программ в каждом компьютере')
    res_2_unsorted = []
    for c in computers:
        # Получаем программы компьютера
        c_programs = list(filter(lambda i: i[2] == c.name, one_to_many))
        if len(c_programs) > 0:
            # Вычисляем средний размер программ без использования mean()
            total_size = sum(size for _, size, _ in c_programs)
            count = len(c_programs)
            avg_size = total_size / count if count > 0 else 0
            res_2_unsorted.append((c.name, round(avg_size, 2)))

    # Сортировка по среднему размеру
    res_2 = sorted(res_2_unsorted, key=itemgetter(1))
    headers_2 = ['Компьютер', 'Средний размер программ (МБ)']
    print_table(headers_2, res_2)

    print('Задание 3')
    print('Список всех компьютеров, у которых название начинается с буквы "А", и список программ, установленных на них')
    res_3 = []
    # Находим компьютеры, начинающиеся на "А"
    a_computers = [c for c in computers if c.name.startswith('А')]

    for c in a_computers:
        # Получаем программы компьютера (связь многие-ко-многим)
        c_programs = list(filter(lambda i: i[2] == c.name, many_to_many))
        c_program_names = [name for name, _, _ in c_programs]
        # Добавляем компьютер даже если нет программ
        if c_program_names:
            for prog_name in c_program_names:
                res_3.append((c.name, prog_name))
        else:
            res_3.append((c.name, 'Нет программ'))

    # Сортировка по названию компьютера
    res_3_sorted = sorted(res_3, key=itemgetter(0))
    headers_3 = ['Компьютер', 'Программа']
    print_table(headers_3, res_3_sorted)


if __name__ == '__main__':
    main()
