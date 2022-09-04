"""
Создать класс BookCard, в классе должны быть:

- private атрибут author - автор (тип str)
- private атрибут title - название книги (тип str)
- private атрибут year - год издания (тип int)
- магический метод __init__, который принимает author, title, year
- магические методы сравнения для сортировки книг по году издания
- сеттеры и геттеры к атрибутам author, title, year. В сеттерах сделать проверку
  на тип данных, если тип данных не подходит, то бросить ValueError. Для года
  издания дополнительно проверить на валидность (> 0, <= текущего года).

Аксессоры реализоваться через property.
"""
from datetime import date

CURRENT_YEAR = date.today().year


class BookCard:
    __author: str
    __title: str
    __year: int

    def __init__(self, author, title, year):
        self.__author = author
        self.__title = title
        self.__year = year

    def __eq__(self, other):
        return(self.__year == other.__year)

    def __ne__(self, other):
        return (self.__year != other.__year)

    def __lt__(self, other):
        return (self.__year < other.__year)

    def __le__(self, other):
        return (self.__year <= other.__year)

    def __gt__(self, other):
        return (self.__year > other.__year)

    def __ge__(self, other):
        return (self.__year >= other.__year)

    @property
    def year(self):
        """
        Возвращаем год - геттер
        """
        return self.__year

    @year.setter
    def year(self, value):
        """
        Устанавливаем ограничения для года книги - сеттер
        """
        if not isinstance(value, int):
            raise ValueError("год должен быть целым числом")
        elif isinstance(value, int):
            if value < 0 or value > CURRENT_YEAR:
                raise ValueError("год должен быть больше 0 и меньше текущего года")
        else:
            self.__year = value

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        if not isinstance(value, str):
            raise ValueError
        else:
            self.__author = value

    @property
    def title(self):
        """
        Возвращаем название книги - геттер
        """
        return self._title

    @title.setter
    def title(self, value):
        """
        Устанавливаем ограничения для названия - сеттер
        """
        if not isinstance(value, str):
            raise ValueError
        else:
            self.__title = value

