from figure import Figure
from color import FigureColor
import math
from colorama import Fore, Style


class Circle(Figure):
    """
    Класс «Круг»
    """

    FIGURE_NAME = "Круг"

    def __init__(self, radius, color):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")

        self._radius = radius
        self.color_property = FigureColor()
        self.color_property.color = color

    @property
    def name(self):
        return self.FIGURE_NAME

    @property
    def radius(self):
        return self._radius

    def square(self):
        """Вычисление площади круга"""
        return math.pi * self._radius ** 2

    def __repr__(self):
        color_code = self.get_color_code()
        return "{}{} {} цвета радиусом {} площадью {:.2f}{}".format(
            color_code,
            self.name,
            self.color_property.color,
            self._radius,
            self.square(),
            Style.RESET_ALL
        )
