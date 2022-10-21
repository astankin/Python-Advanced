from collections import deque

effects = deque(map(int, input().split(", ")))
casings = list(map(int, input().split(", ")))

bombs = {
    40: "Datura",
    60: "Cherry",
    120: "Smoke Decoy"

}
created_bombs = {"Datura": 0, "Cherry": 0, "Smoke Decoy": 0}
bombs_successfully = False
while effects and casings and not bombs_successfully:
    current_effect = effects.popleft()
    current_casing = casings.pop()
    bomb_mix = current_effect + current_casing
    if bomb_mix in bombs:
        created_bombs[bombs[bomb_mix]] += 1
    else:
        casings.append(current_casing - 5)
        effects.appendleft(current_effect)
    for count in created_bombs.values():
        if count < 3:
            break
    else:
        bombs_successfully = True



if bombs_successfully:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if effects:
    print(f"Bomb Effects: {', '.join([str(x) for x in effects])}")
else:
    print("Bomb Effects: empty")
if casings:
    print(f"Bomb Casings: {', '.join([str(x) for x in casings])}")
else:
    print("Bomb Casings: empty")
sorted_created_bombs = sorted(created_bombs.items(), key=lambda x: x[0])
for bomb, count in sorted_created_bombs:
    print(f"{bomb} Bombs: {count}")

