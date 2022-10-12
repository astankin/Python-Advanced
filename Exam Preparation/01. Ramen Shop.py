from collections import deque

bowls_of_ramen = list(map(int, input().split(", ")))
costumers = deque(map(int, input().split(", ")))

while bowls_of_ramen and costumers:
    ramen = bowls_of_ramen.pop()
    current_costumer = costumers.popleft()
    if ramen > current_costumer:
        ramen -= current_costumer
        bowls_of_ramen.append(ramen)
    elif ramen < current_costumer:
        current_costumer -= ramen
        costumers.appendleft(current_costumer)

if not costumers:
    print("Great job! You served all the customers.")
    if bowls_of_ramen:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls_of_ramen)}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in costumers)}")
