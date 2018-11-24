def find_var_by_name(name, variables):
    for i in variables:
        if i.name == name:
            return i
    return None


def defuzzify(rules, variables):
    num = 0
    den = 0
    for i in rules:
        ans = i.evaluate(variables)
        print(ans, i.get_consequent().value)
        output = find_var_by_name(i.get_consequent().var, variables)
        num += ans * output.get_fuzzy_set(i.get_consequent().value).center_x()
        den += ans
    print("Sum of centers:", round(num, 2), "Sum of percentages:", round(den, 2), "C/P", round(num / den, 2))
