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
        return self.__year
    @year.setter
    def year(self, year):
        if isinstance(year, int) and (0 < year <= CURRENT_YEAR):
            self.__year = year
        else:
            raise ValueError

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        if isinstance(author, str):
            self.__author = author
        else:
            raise ValueError

    @property
    def title(self):
        """
        Возвращаем название книги - геттер
        """
        return self.__title

    @title.setter
    def title(self, title):
        """
        Устанавливаем ограничения для названия - сеттер
        """
        if isinstance(title, str):
            self.__title = title
        else:
            raise ValueError





a = BookCard(1,2,3)