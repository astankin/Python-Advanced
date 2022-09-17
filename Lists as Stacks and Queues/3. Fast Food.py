from collections import deque

food_quantity = int(input())
orders = deque(int(x) for x in input().split())

print(max(orders))
while orders:
    order = orders.popleft()
    if order <= food_quantity:
        food_quantity -= order
    else:
        orders.appendleft(order)
        break

if not orders:
    print("Orders complete")
else:
    print(f"Orders left:", *orders, sep=" ")
