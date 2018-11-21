from trapezoid import Trapezoid
from triangle import Triangle


class Variable:
    def __init__(self, name, value=-1):
        self.name = name
        self.value = value

        self.fuzzy_set = []

    def add_fuzzy_set(self, name, values):
        if name == "trapezoidal":
            new_fuzzy_set = Trapezoid(name=name, values=values)
            self.fuzzy_set.append(new_fuzzy_set)
        else:
            new_fuzzy_set = Triangle(name=name, values=values)
            self.fuzzy_set.append(new_fuzzy_set)

    def __str__(self):
        return self.name
