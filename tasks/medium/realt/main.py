from house import *
from townhouse import *
from person import *


if __name__ == '__main__':
    pass

A = House("Minsk", 90, 50)
B = Townhouse("Grodno", 100)
Elena = Person("Elena", 30)

print(Elena.earn_money(150))
Elena.make_deal(A)
print(Elena.money)
print(Elena.realty[0].address)
Elena.make_deal(B)
print(Elena.realty[1].address)
print(Elena.money)
