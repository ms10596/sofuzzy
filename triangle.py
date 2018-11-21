class Triangle:
    def __init__(self, x1, x2, x3, name):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.name = name

        self.m1 = 1 / (x2 - x1)
        self.m2 = -1 / (x3 - x2)
        print(self.m1, self.m2)

    def predict(self, x):
        if self.x1 <= x <= self.x2:
            return self.m1 * (x - self.x1)
        elif self.x2 < x <= self.x3:
            return self.m2 * (x - self.x2) + 1
        else:
            return 0


if __name__ == '__main__':
    t = Triangle(0, 25, 1000)
    for i in range(1000):
        print(i, t.predict(i))
