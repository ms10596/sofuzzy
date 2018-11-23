def inference(rules, variables):
    for i in rules:
        print(i.evaluate(variables))