from collections import deque
n = int(input())
queue = deque()
for _ in range(n):
    data = input().split()
    queue.append([int(data[0]), int(data[1])])

for idx in range(n):
    fuel_tank = 0
    pump_index = 0
    for pump in queue:
        fuel, distance = pump[0], pump[1]
        fuel_tank += fuel
        if fuel_tank < distance:
            break
        fuel_tank -= distance
        pump_index += 1
    if pump_index == len(queue):
        print(idx)
        break
    queue.rotate(-1)

