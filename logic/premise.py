def find_var_by_name(name, variables):
    for i in variables:
        if i.name == name:
            return i
    return None


class Premise:
    def __init__(self, var, value):
        self.var = var
        self.value = value

    def evaluate(self, variables):
        var = find_var_by_name(self.var, variables)
        return round(var.fuzz(self.value), 2)

    def __str__(self):
        return self.var + "=" + self.value
