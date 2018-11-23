class Statement:
    def __init__(self):
        self.premises = []
        self.gates = []

    def add_premise(self, premise):
        self.premises.append(premise)

    def add_gate(self, gate):
        self.gates.append(gate)

    def __str__(self):
        return str([str(i) for i in self.premises])
