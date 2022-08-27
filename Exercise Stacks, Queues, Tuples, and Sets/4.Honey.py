from collections import deque

operator = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}

bees = deque(int(num) for num in input().split())
nectar_amount = [int(num) for num in input().split()]
symbols = deque(input().split())
honey = 0
while bees and nectar_amount:
    bee = bees.popleft()
    nectar = nectar_amount.pop()
    if bee == 0 and nectar == 0:
        continue
    if nectar < bee:
        bees.appendleft(bee)
        continue
    symbol = symbols.popleft()
    honey += abs(operator[symbol](bee, nectar))

print(f"Total honey made: {honey}")
if bees:
    print(f"Bees left: {', '.join(str(num) for num in bees)}")
if nectar_amount:
    print(f"Nectar left: {', '.join(str(num) for num in nectar_amount)}")
