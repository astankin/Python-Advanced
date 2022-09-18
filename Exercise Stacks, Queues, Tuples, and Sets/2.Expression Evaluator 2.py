from collections import deque


def calculation(operator, nums):
    while len(nums) > 1:
        result = 0
        first_num = nums.popleft()
        second_num = nums.popleft()
        if operator == "+":
            result = first_num + second_num
        elif operator == "-":
            result = first_num - second_num
        elif operator == "*":
            result = first_num * second_num
        elif operator == "/":
            result = first_num // second_num
        nums.appendleft(result)
    return nums


line = input().split()
numbers = deque()
for char in line:
    if char not in "-+*/":
        numbers.append(int(char))
    else:
        numbers = calculation(char, numbers)

print(*numbers)

