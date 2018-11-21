from variable import Variable

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
    name = f.readline()
    new_var = Variable(name)
    fuzzy_sets_n = int(f.readline())
    for j in range(fuzzy_sets_n):
        line = f.readline().split()
        name = line[0]
        kind = line[1]

        values = tuple(map(float, f.readline().split()))
        new_var.add_fuzzy_set(name, values)

    variables.append(new_var)
    for i in variables:
        print(i)

