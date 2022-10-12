from functools import reduce

numbers_list = [1, 2, 3]
operator = input()
result = reduce(lambda x, y: eval(f"{x} {operator} {y}"), numbers_list)
print(result)