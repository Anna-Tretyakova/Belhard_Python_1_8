from house import*


class Townhouse(House):

    def __init__(self, address, cost):
        self.address = address
        self.area = 60
        self.cost = cost
