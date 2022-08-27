from collections import deque

chocolates = [int(num) for num in input().split(", ")]
milk_cups = deque(int(num) for num in input().split(", "))
milkshakes = 0
while chocolates and milk_cups:
    chocolate = chocolates.pop()
    milk = milk_cups.popleft()
    if chocolate <= 0 and milk <= 0:
        continue
    if chocolate <= 0:
        milk_cups.appendleft(milk)
        continue
    if milk <= 0:
        chocolates.append(chocolate)
        continue
    if chocolate == milk:
        milkshakes += 1
        if milkshakes == 5:
            break
    else:
        milk_cups.append(milk)
        chocolates.append(chocolate - 5)
if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {', '.join([str(num) for num in chocolates])}")
else:
    print("Chocolate: empty")
if milk_cups:
    print(f"Milk: {', '.join([str(num) for num in milk_cups])}")
else:
    print("Milk: empty")
