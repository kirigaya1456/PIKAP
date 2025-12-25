from rectangle import Rectangle
from circle import Circle
from square import Square
from colorama import Fore, Back, Style, init


def main():
    """
    основная функция программы
    """

    N = 1

    print(Fore.CYAN + "=" * 70)
    print("демонстрация работы с геометрическими фигурами")
    print("используется пакет colorama для цветного вывода")
    print("=" * 70 + Style.RESET_ALL)

    print(Fore.YELLOW + "\nсоздание фигур..." + Style.RESET_ALL)
    rectangle = Rectangle(N, N, "синего")
    circle = Circle(N, "зеленого")
    square = Square(N, "красного")

    print(Fore.YELLOW + "\nсозданные фигуры:" + Style.RESET_ALL)
    print(rectangle)
    print(circle)
    print(square)

    print(Fore.CYAN + "\n" + "=" * 70)
    print("демонстрация работы с пакетом colorama")
    print("=" * 70 + Style.RESET_ALL)

    print(Fore.RED + Style.BRIGHT + "яркий красный текст" + Style.RESET_ALL)
    print(Fore.BLACK + Back.WHITE + "черный текст на белом фоне" + Style.RESET_ALL)
    print(Fore.BLUE + Style.DIM + "тусклый синий текст" + Style.RESET_ALL)

    print(" цветная таблица фигур ")

    figures = [rectangle, circle, square]

    for i, figure in enumerate(figures, 1):
        color_code = figure.get_color_code()
        print("{}[{:2d}] {}{}: площадь = {:.2f}{}".format(
            color_code, i, figure.name, Style.RESET_ALL, figure.square(), Style.RESET_ALL
        ))

    print(Fore.CYAN + "\n" + "=" * 70)
    print("сравнение площадей фигур")
    print("=" * 70 + Style.RESET_ALL)

    max_figure = max(figures, key=lambda f: f.square())
    min_figure = min(figures, key=lambda f: f.square())

    print(Fore.GREEN + Style.BRIGHT + "фигура с наибольшей площадью:" + Style.RESET_ALL)
    print(Fore.GREEN + f"   {max_figure.name}: {max_figure.square():.2f}" + Style.RESET_ALL)

    print(Fore.RED + Style.BRIGHT + "\nфигура с наименьшей площадью:" + Style.RESET_ALL)
    print(Fore.RED + f"   {min_figure.name}: {min_figure.square():.2f}" + Style.RESET_ALL)

    total_area = sum(f.square() for f in figures)
    print(Fore.BLUE + Style.BRIGHT + f"\nобщая площадь всех фигур: {total_area:.2f}" + Style.RESET_ALL)

    print("все цвета colorama")

    colors = [
        (Fore.BLACK, "BLACK", "черный"),
        (Fore.RED, "RED", "красный"),
        (Fore.GREEN, "GREEN", "зеленый"),
        (Fore.YELLOW, "YELLOW", "желтый"),
        (Fore.BLUE, "BLUE", "синий"),
        (Fore.MAGENTA, "MAGENTA", "фиолетовый"),
        (Fore.CYAN, "CYAN", "голубой"),
        (Fore.WHITE, "WHITE", "белый"),
    ]

    for color_code, eng_name, rus_name in colors:
        print("{} {} ({}) - пример текста {}".format(
            color_code, rus_name, eng_name.lower(), Style.RESET_ALL
        ))


if __name__ == "__main__":
    main()
