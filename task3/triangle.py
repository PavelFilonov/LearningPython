import math


class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getAB(self):
        return math.sqrt(math.pow(self.b.x - self.a.x, 2) + math.pow(self.b.y - self.a.y, 2))

    def getBC(self):
        return math.sqrt(math.pow(self.c.x - self.b.x, 2) + math.pow(self.c.y - self.b.y, 2))

    def getAC(self):
        return math.sqrt(math.pow(self.c.x - self.a.x, 2) + math.pow(self.c.y - self.a.y, 2))

    def get(self):
        return self.a.get() + "; " + self.b.get() + "; " + self.c.get()
