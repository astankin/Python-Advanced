from collections import deque

cups = deque(int(num) for num in input().split())
bottles = [int(num) for num in input().split()]
waste_water = 0
while bottles and cups:
    cup = cups.popleft()
    while cup > 0:
        bottle = bottles.pop()
        if bottle >= cup:
            waste_water += bottle - cup
            cup -= bottle
        else:
            cup -= bottle
if bottles:
    print(f"Bottles: {' '.join(str(el)for el in bottles)}")
if cups:
    print(f"Cups: {' '.join(str(el)for el in cups)}")
print(f"Wasted litters of water: {waste_water}")
