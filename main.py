from file_operations import read_variables, read_rules
from defuzzification import defuzzify

if __name__ == '__main__':
    f = open('sample.txt')
    variables = read_variables(f)
    rules = read_rules(f)
    print("Fuzzification:")
    [i.fuzzify() for i in variables]
    print("\n\nInference:")
    [i.print_evaluate(variables) for i in rules]
    print("\n\nDefuzzification:")
    defuzzify(rules, variables)
