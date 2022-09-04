class Tomato:
    index: int
    ripeness: str
    states: set

    def __init__(self, index):
        self.index = index
        states = ("Отсутствует", "Цветение", "Зеленый", "Красный")
        self.states = states
        self.ripeness = list(self.states)[0]

    def grow(self):
        i = list(self.states).index(self.ripeness)
        if i < (len(self.states) - 1):
            self.ripeness = list(self.states)[i + 1]
        return self

    def is_ripe(self):
         return list(self.states).index(self.ripeness) == len(self.states) - 1



