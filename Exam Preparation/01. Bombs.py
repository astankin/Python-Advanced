from collections import deque

effects = deque(map(int, input().split(", ")))
casing = list(map(int, input().split(", ")))

bombs = {
    40: "Datura Bombs",
    60: "Cherry Bombs",
    120: "Smoke Decoy Bombs"
}

created_bombs = {
    "Datura Bombs": 0,
    "Cherry Bombs": 0,
    "Smoke Decoy Bombs": 0
}
condition = False
while effects and casing:
    current_effect = effects.popleft()
    current_casing = casing.pop()
    mix = current_casing + current_effect
    if mix in bombs:
        created_bombs[bombs[mix]] += 1
    else:
        casing.append(current_casing - 5)
        effects.appendleft(current_effect)
    for bomb in created_bombs.values():
        if bomb < 3:
            condition = False
            break
        else:
            condition = True
    if condition:
        break

if condition:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")


if effects:
    print(f"Bomb Effects: {', '.join(map(str, effects))}")
else:
    print("Bomb Effects: empty")

if casing:
    print(f"Bomb Casings: {', '.join(map(str, casing))}")
else:
    print("Bomb Casings: empty")


sorted_bombs = sorted(created_bombs.items(), key=lambda x: x[0])

for bomb, count in sorted_bombs:
    print(f"{bomb}: {count}")
