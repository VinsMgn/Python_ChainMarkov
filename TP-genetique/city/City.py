import math


class City:

    def __init__(self, name, x, y):
        super().__init__()
        self.name = name
        self.x = x
        self.y = y

    def calculateDistance(self, city):
        dist = math.sqrt((city.x - self.x)**2 + (city.y - self.y)**2)
        return dist
