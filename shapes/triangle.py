from shapes import Polygon


class Triangle(Polygon):
    def __init__(self, values, name):
        """0.1 is added to eliminate division by zero"""
        self.x = values

        self.y = [0, 1, 0]
        self.name = name

        self.m1 = (self.y[1] - self.y[0]) / (self.x[1] + 0.1 - self.x[0])
        self.m2 = (self.y[2] - self.y[1]) / (self.x[2] + 0.1 - self.x[1])

    def predict(self, x):
        if self.x[0] <= x <= self.x[1]:
            return self.m1 * (x - self.x[0])
        elif self.x[1] < x <= self.x[2]:
            return self.m2 * (x - self.x[1]) + 1
        else:
            return 0

    def __str__(self):
        return "Triangle " + str(self.x)
