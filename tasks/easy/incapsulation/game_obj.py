"""
Напишите класс GameObject, в котором будут храниться координаты объекта.

- private атрибут x (тип int)
- private атрибут y (тип int)
- магический метод __init__, который принимает начальные x и y

Координаты должны быть доступны для чтения (сделать property), а их изменение
должно происходить в методе move(delta_x, delta_y). (изменение - это +=)
"""


class GameObject:
    _x: int
    _y: int
    def __init__(self, x, y):
        self._x = x

        self._y = y

    @property
    def _x(self):
        return self._x

    @property
    def _y(self):
        return self._y

    def move(self, delta):
        delta = input(delta)
        self._x += delta
        self._y += delta
        return self._x
        return self._y
