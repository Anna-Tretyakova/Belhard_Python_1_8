from tomato import *


class TomatoBush:
    tomato_list: []

    def __init__(self, *args):
        tomato_list = []
        for i in args:
            tomato_list.append(i)
            self.tomato_list = tomato_list

    def grow_all(self):
        n = len(self.tomato_list)
        for a in range(0, n):
            self.tomato_list[a].grow()
            a += 1
        return self.tomato_list

    def all_are_ripe(self):
        list_2 = []
        for i in self.tomato_list:
            if i.is_ripe() is True:
                list_2.append(i)
                return bool(len(list_2) == len(self.tomato_list))

    def give_away_all(self):
        print(self.tomato_list)
        self.tomato_list.clear()




