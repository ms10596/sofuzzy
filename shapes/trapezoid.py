from shapes import Polygon


class Trapezoid(Polygon):
    def __init__(self, values, name):
        """0.1 is added to eliminate division by zero"""
        self.x = values
        self.name = name

        self.y = [0, 1, 1, 0]
        self.m1 = (self.y[1] - self.y[0]) / (self.x[1] + 0.1 - self.x[0])
        self.m2 = 0
        self.m3 = (self.y[3] - self.y[2]) / (self.x[3] + 0.1 - self.x[2])

    def predict(self, x):
        if self.x[0] <= x < self.x[1]:
            return self.m1 * (x - self.x[0])
        elif self.x[1] <= x <= self.x[2]:
            return 1
        elif self.x[2] < x <= self.x[3]:
            return self.m3 * (x - self.x[2]) + 1
        else:
            return 0

    def __str__(self):
        return "Trapezoid " + str([self.x[0], self.x[1], self.x[2], self.x[3]])
