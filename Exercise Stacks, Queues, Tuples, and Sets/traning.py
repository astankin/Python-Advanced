from collections import deque


def calculation(operator, nums):
    if operator == "+":
        result = 0
        for num in nums:
            result += num
        return result
    elif operator == "-":
        result = nums[0]
        for i in range(1, len(nums)):
            result -= nums[i]
        return result
    elif operator == "*":
        result = 1
        for num in nums:
            result *= num
        return result
    elif operator == "/":
        result = nums[0]
        for i in range(1, len(nums)):
            result = result // nums[i]
        return result


line = input().split()
numbers = deque()
output = 0
for char in line:
    if char not in "-+*/":
        numbers.append(int(char))
    else:
        output = calculation(char, numbers)
        numbers.clear()
        numbers.appendleft(output)

print(output)

