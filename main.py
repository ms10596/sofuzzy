from variable import Variable
from premise import Premise
from rule import Rule

if __name__ == '__main__':
    f = open('sample.txt')
    variables = []
    vars_n = int(f.readline())
    for i in range(vars_n):
        line = f.readline().split()
        name = line[0]
        value = float(line[1])
        new_var = Variable(name, value)
        fuzzy_sets_n = int(f.readline())
        for j in range(fuzzy_sets_n):
            line = f.readline().split()
            name = line[0]
            kind = line[1]

            values = tuple(map(float, f.readline().split()))
            new_var.add_fuzzy_set(name, values)
        variables.append(new_var)
    name = f.readline().split()[0]
    new_var = Variable(name)
    fuzzy_sets_n = int(f.readline())
    for i in range(fuzzy_sets_n):
        line = f.readline().split()
        name = line[0]
        kind = line[1]

        values = tuple(map(float, f.readline().split()))
        new_var.add_fuzzy_set(name, values)

    variables.append(new_var)

    rules_n = int(f.readline())
    rules = []
    for i in range(rules_n):
        new_rule = Rule()
        line = f.readline().split()
        premises_n = int(line[0])
        for j in range(premises_n):
            first_premise = Premise(line[1 + j * 4], line[3 + j * 4])
            new_rule.add_premise(first_premise)
            if j < premises_n - 1:
                gate = line[4 + j]
                new_rule.add_premise(gate)
        last_premise = Premise(line[len(line) - 3], line[len(line) - 1])
        new_rule.add_premise(last_premise)

        rules.append(new_rule)
    print("fuzzification: ")
    # [i.fuzzify() for i in variables]
    # print(variables[0].fuzz('Right'))
