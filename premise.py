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
        return var.fuzz(self.value)

    def __str__(self):
        return self.var + "=" + self.value
