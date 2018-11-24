class Trapezoid:
    def __init__(self, values, name):
        self.x = values
        self.name = name

        self.y = [0, 1, 1, 0]
        self.m1 = 1 / (self.x[1] + 0.1 - self.x[0])
        self.m2 = 0
        self.m3 = -1 / (self.x[3] + 0.1 - self.x[2])

    def predict(self, x):
        if self.x[0] <= x < self.x[1]:
            return self.m1 * (x - self.x[0])
        elif self.x[1] <= x <= self.x[2]:
            return 1
        elif self.x[2] < x <= self.x[3]:
            return self.m3 * (x - self.x[2]) + 1
        else:
            return 0

    def area(self):
        total = 0
        for i in range(len(self.x) - 1):
            total += (self.x[i] * self.y[i + 1] - self.x[i + 1] * self.y[i])
        return abs(total) / 2

    def center_x(self):
        total = 0
        for i in range(len(self.x) - 1):
            total += (self.x[i] + self.x[i + 1]) * abs(self.x[i] * self.y[i + 1] - self.x[i + 1] * self.y[i])
        return total / (6 * self.area())

    def center_y(self):
        total = 0
        for i in range(len(self.x) - 1):
            total += (self.y[i] + self.y[i + 1]) * abs(self.x[i] * self.y[i + 1] - self.x[i + 1] * self.y[i])
        return total / (6 * self.area())

    def __str__(self):
        return "Trapezoid " + str([self.x[0], self.x[1], self.x[2], self.x[3]])


if __name__ == '__main__':
    t = Trapezoid((0, 0, 10, 10), "trap")
    print(t.area())
    print(t.center_x())
    print(t.center_y())
    # for i in range(0, 103):
    #     print(i, t.predict(i))
