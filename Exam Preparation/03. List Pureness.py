from collections import deque


def best_list_pureness(*args):
    numbers = deque(args[0])
    k = args[1]
    the_best_pureness = 0
    count_rotations = 0
    for i in range(k + 1):
        nums_sum = 0
        for idx, num in enumerate(numbers):
            nums_sum += idx * num
        if nums_sum > the_best_pureness:
            the_best_pureness = nums_sum
            count_rotations = i
        numbers.appendleft(numbers.pop())
    return f"Best pureness {the_best_pureness} after {count_rotations} rotations"



test = ([2, 2, 2, 2], 4)
result = best_list_pureness(*test)
print(result)


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
