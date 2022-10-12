from collections import deque

pizza_orders = deque(int(x) for x in input().split(", "))
employees = [int(x) for x in input().split(", ")]
total_pizza_made = 0
while pizza_orders and employees:
    order = pizza_orders.popleft()
    if order > 10:
        continue
    if order <= 0:
        continue
    employee_capacity = employees.pop()
    if order <= employee_capacity:
        total_pizza_made += order
    elif order > employee_capacity:
        total_pizza_made += employee_capacity
        order -= employee_capacity
        pizza_orders.appendleft(order)

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizza_made}")

if employees:
    print(f"Employees: {', '.join(map(str, employees))}")

if not employees and pizza_orders:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(map(str, pizza_orders))}")
