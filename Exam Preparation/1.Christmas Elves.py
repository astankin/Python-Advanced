from collections import deque

elfs = deque(int(x) for x in input().split())
boxes = list(int(x) for x in input().split())
created_toys = 0
total_used_energy = 0
counter = 1
while elfs and boxes:
    current_energy = elfs.popleft()
    if current_energy < 5:
        continue
    current_box = boxes.pop()
    reward = 1
    needed_energy = current_box
    toys = 1
    if counter % 3 == 0:
        needed_energy = current_box * 2
        toys = 2
    if current_energy >= needed_energy:
        if counter % 5 == 0:
            toys = 0
            reward = 0
        total_used_energy += needed_energy
        created_toys += toys
        current_energy -= needed_energy
        current_energy += reward
        elfs.append(current_energy)
    else:
        boxes.append(current_box)
        elfs.append(current_energy * 2)

    counter += 1


print(f"Toys: {created_toys}")
print(f"Energy: {total_used_energy}")
if elfs:
    print(f"Elves left: {', '.join(map(str, elfs))}")
if boxes:
    print(f"Boxes left: {', '.join(map(str, boxes))}")



