class Triangle:
    def __init__(self, values, name):
        self.x1 = values[0]
        self.x2 = values[1]
        self.x3 = values[2]

        self.y1 = self.y3 = 0
        self.y2 = 1
        self.name = name

        self.m1 = 1 / (self.x2 + 0.1 - self.x1)
        self.m2 = -1 / (self.x3 + 0.1 - self.x2)
        # print(self.m1, self.m2)

    def predict(self, x):
        if self.x1 <= x <= self.x2:
            return self.m1 * (x - self.x1)
        elif self.x2 < x <= self.x3:
            return self.m2 * (x - self.x2) + 1
        else:
            return 0

    def area(self):
        return 0.5 * (self.x1 * self.y2 - self.x2 * self.y1 + self.x2 * self.y3 - self.x3 * self.y2)

    def __str__(self):
        return "Triangle " + str([self.x1, self.x2, self.x3])


if __name__ == '__main__':
    t = Triangle(0, 25, 1000)
    for i in range(1000):
        print(i, t.predict(i))
