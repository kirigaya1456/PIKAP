from rectangle import Rectangle
from colorama import Fore, Style


class Square(Rectangle):
    """
    Класс «Квадрат» наследуется от класса «Прямоугольник»
    """

    FIGURE_NAME = "Квадрат"

    def __init__(self, side, color):
        super().__init__(side, side, color)

    @property
    def name(self):
        return self.FIGURE_NAME

    @property
    def side(self):
        return self.width

    def __repr__(self):
        color_code = self.get_color_code()
        return "{}{} {} цвета со стороной {} площадью {:.2f}{}".format(
            color_code,
            self.name,
            self.color_property.color,
            self.width,
            self.square(),
            Style.RESET_ALL
        )
