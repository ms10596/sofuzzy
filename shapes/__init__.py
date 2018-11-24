class Polygon:
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
