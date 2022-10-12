numbers_list = [int(x) for x in input().split(", ")]
result = 1

for number in numbers_list:
    if number <= 5:
        result *= number
    elif 5 < number <= 10:
        result /= number
result = str(result)
try:
    value_after_point = result.split(".")[1]
    if int(value_after_point) == 0:
        print(result.split(".")[0])
    else:
        print(result)
except IndexError:
    print(result)

