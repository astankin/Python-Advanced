from collections import deque

chocolates = list(map(int, input().split(', ')))
milk_cups = deque(map(int, input().split(', ')))
milk_shakes = 0
while milk_cups and chocolates and milk_shakes < 5:
    chocolate = chocolates.pop()
    milk = milk_cups.popleft()
    if milk <= 0 >= chocolate:
        continue
    if chocolate <= 0:
        milk_cups.appendleft(milk)
        continue
    if milk <= 0:
        chocolates.append(chocolate)
        continue
    if chocolate != milk:
        milk_cups.append(milk)
        chocolates.append(chocolate - 5)
        continue
    milk_shakes += 1
if milk_shakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {', '.join(str(x) for x in chocolates)}")
else:
    print("Chocolate: empty")
if milk_cups:
    print(f"Milk: {', '.join(str(x) for x in milk_cups)}")
else:
    print("Milk: empty")



