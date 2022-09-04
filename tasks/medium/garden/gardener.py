from tomato_bush import *


class Gardener:
    name: str
    plants: []

    def __init__(self, name, *args):
        self.name = name
        plants = []
        for i in args:
            plants.append(i)
        self.plants = plants

    def work(self):
        for i in range(0, len(self.plants)):
            self.plants[i].grow_all()
        return self.plants

    def harvest(self):
        list_3 = []
        for i in self.plants:
            if i.all_are_ripe is True:
                list_3.append(i)
        if bool(len(list_3) == len(self.plants)) is True:
            a = 0
            for j in range(0, len(self.plants)):
                a += len(self.plants[j])
                return a
        else:
            print("Томаты не созрели")


