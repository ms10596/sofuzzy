from variable import Variable
from premise import Premise
from statement import Statement

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
    statements = []
    for i in range(rules_n):
        new_statement = Statement()
        line = f.readline().split()
        premises_n = int(line[0])
        first_premise = Premise(line[1], line[3])
        gate = line[4]
        second_premise = Premise(line[5], line[7])
        output_premise = Premise(line[8], line[10])
        new_statement.add_premise(first_premise)
        new_statement.add_premise(second_premise)
        new_statement.add_premise(output_premise)
        statements.append(new_statement)
    print([str(i) for i in statements])
