class Premise:
    def __init__(self, var_name, val_name):
        self.var_name = var_name
        self.val_name = val_name

    def __str__(self):
        return self.var_name + "=" + self.val_name
