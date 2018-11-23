class Rule:
    def __init__(self):
        self.premises = []
        # self.gates = []

    def add_premise(self, premise):
        self.premises.append(premise)

    # def add_gate(self, gate):
    #     self.gates.append(gate)
    def evaluate(self, variables):
        if self.premises[1] == 'AND':
            return min(self.premises[0].evaluate(variables), self.premises[2].evaluate(variables))
        elif self.premises[1] == 'OR':
            return max(self.premises[0].evaluate(variables), self.premises[2].evaluate(variables))

    def __str__(self):
        return str([str(i) for i in self.premises])
