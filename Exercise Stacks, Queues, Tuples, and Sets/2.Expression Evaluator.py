from collections import deque
import math
import operator


def calc(op, nums):
    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a // b,
    }

    # ops = {
    #     "+": operator.add,
    #     "-": operator.sub,
    #     "*": operator.mul,
    #     "/": operator.truediv
    # }
    first_num = nums.popleft()
    while len(nums) > 0:
        result = ops[op](first_num, nums.popleft())
        first_num = result
    nums.appendleft(math.floor(first_num))
    return nums


operators = ['+', '-', '*', '/']

string = input().split()
nums = deque()
for char in string:
    if char not in operators:
        nums.append(int(char))
    else:
        nums = calc(char, nums)

print(*nums)
