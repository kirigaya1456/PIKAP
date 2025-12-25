# используется для сортировки
from operator import itemgetter


# класс Пользователь
class User:
    def __init__(self, id, fio, sal, comp_id):
        self.id = id
        self.fio = fio
        self.sal = sal
        self.comp_id = comp_id


# класс Компьютер
class Computer:
    def __init__(self, id, name):
        self.id = id
        self.name = name


# класс для связи многие ко многим
class UserComputer:
    def __init__(self, comp_id, user_id):
        self.comp_id = comp_id
        self.user_id = user_id


# Компьютеры
computers = [
    Computer(1, 'рабочая станция инженера'),
    Computer(2, 'сервер хранения данных'),
    Computer(3, 'ноутбук руководителя'),
    Computer(11, 'графическая станция дизайнера'),
    Computer(22, 'терминал для тестирования'),
    Computer(33, 'мобильная рабочая станция'),
]

# Пользователи
users = [
    User(1, 'Кузнецов', 25000, 1),
    User(2, 'Смирнов', 35000, 2),
    User(3, 'Попов', 45000, 3),
    User(4, 'Васильев', 35000, 3),
    User(5, 'Павлов', 25000, 3),
]

users_computers = [
    UserComputer(1, 1),
    UserComputer(2, 2),
    UserComputer(3, 3),
    UserComputer(3, 4),
    UserComputer(3, 5),
    UserComputer(11, 1),
    UserComputer(22, 2),
    UserComputer(33, 3),
    UserComputer(33, 4),
    UserComputer(33, 5),
]


# функция для вывода результатов
def print_table(headers, data):
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
    one_to_many = [(u.fio, u.sal, c.name)
                   for c in computers
                   for u in users
                   if u.comp_id == c.id]

    many_to_many_temp = [(c.name, uc.comp_id, uc.user_id)
                         for c in computers
                         for uc in users_computers
                         if c.id == uc.comp_id]

    many_to_many = [(u.fio, u.sal, comp_name)
                    for comp_name, comp_id, user_id in many_to_many_temp
                    for u in users if u.id == user_id]

    print('Задание 1')
    print('Список всех связанных пользователей и компьютеров (сортировка по компьютерам)')
    res_11 = sorted(one_to_many, key=itemgetter(2))
    headers_A1 = ['Фамилия', 'Зарплата', 'Компьютер']
    print_table(headers_A1, res_11)

    print('Задание 2')
    print('Список компьютеров с суммарной зарплатой пользователей')
    res_12_unsorted = []
    for c in computers:
        c_users = list(filter(lambda i: i[2] == c.name, one_to_many))
        if len(c_users) > 0:
            c_sals = [sal for _, sal, _ in c_users]
            c_sals_sum = sum(c_sals)
            res_12_unsorted.append((c.name, c_sals_sum))

    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    headers_A2 = ['Компьютер', 'Суммарная зарплата']
    print_table(headers_A2, res_12)

    print('Задание 3')
    print('Компьютеры с названием содержащим "станция" и их пользователи')
    res_13 = []
    for c in computers:
        if 'станция' in c.name:
            c_users = list(filter(lambda i: i[2] == c.name, many_to_many))
            c_users_names = [x for x, _, _ in c_users]
            for user_name in c_users_names:
                res_13.append((c.name, user_name))

    headers_A3 = ['Компьютер', 'Пользователь']
    print_table(headers_A3, res_13)


if __name__ == '__main__':
    main()
