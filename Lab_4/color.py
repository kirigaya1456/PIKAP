class FigureColor:
    """
    Класс «Цвет фигуры»
    """

    def __init__(self):
        self._color = None

    @property
    def color(self):
        """Getter для цвета"""
        return self._color

    @color.setter
    def color(self, value):
        """Setter для цвета"""
        if not isinstance(value, str):
            raise ValueError("Цвет должен быть строкой")
        self._color = value

    def get_color(self):
        """Метод для получения цвета"""
        return self._color

    def set_color(self, value):
        """Метод для установки цвета"""
        self.color = value
