from collections import deque

cups = deque(map(int, input().split()))
bottles = list(map(int, input().split()))
wasted_water = 0
while cups and bottles:
    cup = cups.popleft()
    bottle = bottles.pop()
    if bottle >= cup:
        wasted_water += bottle - cup
    cup -= bottle
    if cup > 0:
        cups.appendleft(cup)
        continue
if not cups and bottles:
    print(f"Bottles:", *bottles, sep=' ')
if cups:
    print(f"Cups:", *cups, sep=' ')
print(f"Wasted litters of water: {wasted_water}")
