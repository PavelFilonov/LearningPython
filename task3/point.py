class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
