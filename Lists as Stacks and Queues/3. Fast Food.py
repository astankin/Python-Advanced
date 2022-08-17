from collections import deque

food_quantity = int(input())
orders = deque((map(int, input().split())))
print(max(orders))
for i in range(len(orders)):
    order = orders.popleft()
    if food_quantity >= order:
        food_quantity -= order
    else:
        orders.appendleft(order)
        break
if not orders:
    print("Orders complete")
else:
    print(f"Orders left:", *orders, sep=" ")

