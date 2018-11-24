from shapes.trapezoid import Trapezoid
from shapes.triangle import Triangle


class Variable:
    def __init__(self, name, value=-1):
        self.name = name
        self.value = value

        self.fuzzy_set = []

    def add_fuzzy_set(self, name, values):
        if len(values) == 4:
            new_fuzzy_set = Trapezoid(name=name, values=values)
            self.fuzzy_set.append(new_fuzzy_set)
        else:
            new_fuzzy_set = Triangle(name=name, values=values)
            self.fuzzy_set.append(new_fuzzy_set)

    def fuzzify(self):
        print(self.name, "=", self.value)
        for i in self.fuzzy_set:
            print('\t', i.name, "=", round(i.predict(self.value), 2))

    def fuzz(self, set_name):
        for i in self.fuzzy_set:
            if i.name == set_name:
                return i.predict(self.value)

    def get_fuzzy_set(self, set_name):
        for i in self.fuzzy_set:
            if i.name == set_name:
                return i
        return None

    def __str__(self):
        return self.name + str([str(i) for i in self.fuzzy_set])
