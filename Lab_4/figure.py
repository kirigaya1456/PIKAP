from abc import ABC, abstractmethod
from colorama import Fore, Style


class Figure(ABC):
    """
    Абстрактный класс «Геометрическая фигура»
    """

    @property                     #свойство
    @abstractmethod
    def name(self):
        """Название фигуры"""
        pass

    @abstractmethod
    def square(self):
        """
        Абстрактный метод для вычисления площади фигуры.
        """
        pass

    def get_color_code(self):
        """Возвращает цветовой код для фигуры"""
        color_mapping = {
            'синего': Fore.BLUE,
            'зеленого': Fore.GREEN,
            'красного': Fore.RED,
            'желтого': Fore.YELLOW,
            'фиолетового': Fore.MAGENTA,
            'голубого': Fore.CYAN
        }
        return color_mapping.get(getattr(self, 'color_property', None).color, Fore.WHITE)
