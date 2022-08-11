from collections import deque

water_quantity = int(input())
name = input()
queue = deque()
while not name == "Start":
    queue.append(name)
    name = input()
command = input()
while not command == "End":
    if command.isdigit():
        liters = int(command)
        if water_quantity >= liters:
            water_quantity -= liters
            print(f"{queue.popleft()} got water")

        else:
            print(f"{queue.popleft()} must wait")
    else:
        liters = int(command.split()[1])
        water_quantity += liters
    command = input()
print(f"{water_quantity} liters left")
