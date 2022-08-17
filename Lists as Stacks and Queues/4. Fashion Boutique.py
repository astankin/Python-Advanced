from collections import deque

clothes = deque(map(int, input().split()))
rack_capacity = int(input())
items_sum = 0
number_of_racks = 1
while clothes:
    item = clothes.pop()
    if items_sum + item > rack_capacity:
        number_of_racks += 1
        items_sum = 0
    items_sum += item

print(number_of_racks)