class Trapezoid:
    def __init__(self, values, name):
        self.x1 = values[0]
        self.x2 = values[1]
        self.x3 = values[2]
        self.x4 = values[3]
        self.name = name

        self.m1 = 1 / (self.x2 + 0.1 - self.x1)
        self.m2 = 0
        self.m3 = -1 / (self.x4 + 0.1 - self.x3)

    def predict(self, x):
        if self.x1 <= x < self.x2:
            return self.m1 * (x - self.x1)
        elif self.x2 <= x <= self.x3:
            return 1
        elif self.x3 < x <= self.x4:
            return self.m3 * (x - self.x3) + 1
        else:
            return 0

    def __str__(self):
        return "Trapezoid " + str([self.x1, self.x2, self.x3, self.x4])


if __name__ == '__main__':
    t = Trapezoid(65, 90, 100, 100)
    for i in range(0, 103):
        print(i, t.predict(i))
