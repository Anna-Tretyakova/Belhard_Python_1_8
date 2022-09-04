from tomato import *
from tomato_bush import *
from gardener import *

if __name__ == '__main__':
    pass
t_1 = Tomato(1)
t_2 = Tomato(2)
t_3 = Tomato(3)
t_4 = Tomato(4)
bush_1 = TomatoBush(t_1, t_2)
bush_1.grow_all()
print(t_2.ripeness)
bush_2 = TomatoBush(t_3, t_4)
J = Gardener("John", bush_1, bush_2)
J.work()
J.work()
J.work()
J.work()
print(t_4.ripeness)
print(t_1.ripeness)
print(t_3.ripeness)
J.harvest()
