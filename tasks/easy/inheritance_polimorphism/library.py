"""
Определить класс Person:

- атрибут fullname - ФИО (тип str)
- атрибут phone - номер телефона (тип str)
- магический метод __init__, который принимает fullname и phone

Описать класс LibraryReader, который наследуется от Person:

- атрибут uid - номер читательского билета (тип int)
- атрибут books - список книг (тип set)
- магический метод __init__, который принимает fullname, phone, uid, а books
  заполняет пустым множеством
- метод take_books(*args), который принимает произвольное количество книг
  (книга - строка с названием книги) и возвращает строку: "Петров В.В. взял(а)
  книги: Приключения, Словарь, Энциклопедия", если было взято до 3 книг
  включительно. Если было взято больше книг, то возвращает строку: "Петров В.В.
  взял(а) 4 книги".
- метод return_book(*args), который принимает произвольное количество книг
  (книга - строка с названием книги) и возвращает строку: "Петров В.В. вернул(а)
  книги: Приключения, Словарь, Энциклопедия", если было возвращено до 3 книг
  включительно. Если было возвращено больше книг, то возвращает строку:
  "Петров В.В. вернул(а) 4 книги". Если какой-то книги нет, то бросить исключение
  ValueError с сообщением "Петров В. В. не брал: Рассказы", при этом книги не
  должны быть удалены

Названия книг в сообщениях должны быть отсортированы по алфавиту.
"""


class Person:
    fullname: str
    phone: str

    def __init__(self, fullname, phone):
        self.fullname = fullname
        self.phone = phone


class LibraryReader(Person):
    uid: int
    books: set

    def __init__(self, fullname, phone, uid):
        self.fullname = fullname
        self.phone = phone
        self.uid = uid
        self.books = ()

    def take_books(self, *args):
        list_1 = []
        for i in args:
            list_1.append(i)
            list_1.sort()
            self.books = set(list_1)
        if len(list_1) == 1:
            return(f"{self.fullname} взял(а) книги: {list_1[0]}")
        elif len(list_1) == 2:
            return (f"{self.fullname} взял(а) книги: {list_1[0]},{list_1[1]}")
        elif len(list_1) == 3:
            return (f"{self.fullname} взял(а) книги: {list_1[0]},{list_1[1]},{list_1[2]}")
        elif len(list_1) > 3:
            return (f"{self.fullname} взял(а) 4 книги")

    def return_book(self, *args):
        list_2 = []
        for i in args:
            if i not in self.books:
                raise ValueError(f"{self.fullname} не брал:{i}")
            else:
                list_2.append(i)
                list_2.sort()
                self.books = self.books.difference(set(list_2))
        if len(list_2) == 1:
            return (f"{self.fullname} вернул(а) книги: {list_2[0]}")
        elif len(list_2) == 2:
            return (f"{self.fullname} вернул(а) книги: {list_2[0]},{list_2[1]}")
        elif len(list_2) == 3:
            return (f"{self.fullname} вернул(а) книги: {list_2[0]},{list_2[1]},{list_2[2]}")
        elif len(list_2) > 3:
            return (f"{self.fullname} вернул(а) 4 книги")


a = LibraryReader("AnnaT", 3316835, 331)
library_reader = LibraryReader("Fullname", "375557894545", 123)
print(library_reader.fullname)
print(library_reader.phone)
print(library_reader.uid)
print(library_reader.books)

print(library_reader.take_books("Азбука", "Буратино","Весна", "Дом у озера", "Оно", "Страна радости"))

print(library_reader.books)
