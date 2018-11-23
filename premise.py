class Premise:
    def __init__(self, var, value):
        self.var = var
        self.value = value

    def __str__(self):
        return self.var + "=" + self.value
