from house import *
from townhouse import *


class Person:
    name = str
    age: int
    money: int
    realty: list

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.money = 0
        self.realty = []

    def info(self):
        print(self.name)
        print(self.age)
        print(self.money)
        print(self.realty)

    def earn_money(self, c):
        self.money = self.money + c
        return self.money

    def make_deal(self, obj):
        if self.money >= obj.cost:
            self.money = self.money - obj.cost
            self.realty.append(obj)
        else:
            print("Недостаточно денег")
