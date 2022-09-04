class House:
    address: str
    area: int
    cost: int

    def __init__(self, address, area, cost):
        self.address = address
        self.area = area
        self.cost = cost

    def increase_cost(self, a):
        self.cost = self.cost + a
        return self.cost

    def decrease_cost(self, b):
        self.cost = self.cost - b
        return self.cost
