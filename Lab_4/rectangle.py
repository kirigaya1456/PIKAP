from figure import Figure
from color import FigureColor
from colorama import Fore, Style


class Rectangle(Figure):
    """
    Класс «Прямоугольник»
    """

    FIGURE_NAME = "Прямоугольник"

    def __init__(self, width, height, color):
        if width <= 0 or height <= 0:
            raise ValueError("Ширина и высота должны быть положительными числами")

        self._width = width
        self._height = height
        self.color_property = FigureColor()
        self.color_property.color = color

    @property
    def name(self):
        return self.FIGURE_NAME

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def square(self):
        """Вычисление площади прямоугольника"""
        return self._width * self._height

    def __repr__(self):
        color_code = self.get_color_code()
        return "{}{} {} цвета шириной {} и высотой {} площадью {:.2f}{}".format(
            color_code,
            self.name,
            self.color_property.color,
            self._width,
            self._height,
            self.square(),
            Style.RESET_ALL
        )
