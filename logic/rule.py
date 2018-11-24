class Rule:
    def __init__(self):
        self.premises = []

    def __str__(self):
        return str([str(i) for i in self.premises])

    def add_premise(self, premise):
        self.premises.append(premise)

    def get_consequent(self):
        return self.premises[-1]

    def print_evaluate(self, variables):
        print(self)
        if self.premises[1] == 'AND':
            print("\tmin(", self.premises[0], ",", self.premises[2], ")")
            print("\tmin(", self.premises[0].evaluate(variables), ",", self.premises[2].evaluate(variables),
                  ") =", min(self.premises[0].evaluate(variables), self.premises[2].evaluate(variables)),
                  self.premises[3].value)
            # return min(self.premises[0].evaluate(variables), self.premises[2].evaluate(variables))

        elif self.premises[1] == 'OR':
            print("\tmax(", self.premises[0], ",", self.premises[2], ")")
            print("\tmax(", self.premises[0].evaluate(variables), ",", self.premises[2].evaluate(variables),
                  ") =", max(self.premises[0].evaluate(variables), self.premises[2].evaluate(variables)),
                  self.premises[3].value)
            # return max(self.premises[0].evaluate(variables), self.premises[2].evaluate(variables))

    def evaluate(self, variables):
        if self.premises[1] == 'AND':
            return min(self.premises[0].evaluate(variables), self.premises[2].evaluate(variables))
        elif self.premises[1] == 'OR':
            return max(self.premises[0].evaluate(variables), self.premises[2].evaluate(variables))
