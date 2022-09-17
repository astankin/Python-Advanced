def operate(operator, *args):
    result = 0 if operator in '+-' else 1
    if operator == "+":
        result = sum(args)
    elif operator == "*":
        for num in args:
            result *= int(num)
    elif operator == "-":
        result = args[0]
        for i in range(1, len(args)):
            result -= args[i]
    elif operator == "/":
        result = args[0]
        for i in range(1, len(args)):
            result /= int(args[i])

    return result


print(operate("+", 1, 2, 3))
print(operate("-", 3, 4))
