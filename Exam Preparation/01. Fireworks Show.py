from collections import deque

firework_effects = deque(int(x) for x in input().split(", "))
explosive_power = [int(x) for x in input().split(", ")]

created_fireworks = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0
}
condition = False
while firework_effects and explosive_power:

    effect = firework_effects.popleft()
    if effect <= 0:
        continue
    power = explosive_power.pop()
    if power <= 0:
        firework_effects.appendleft(effect)
        continue

    firework_sum = effect + power
    if firework_sum % 3 == 0 and firework_sum % 5 == 0:
        created_fireworks["Crossette Fireworks"] += 1
    elif firework_sum % 3 == 0 and firework_sum % 5 != 0:
        created_fireworks["Palm Fireworks"] += 1
    elif firework_sum % 3 != 0 and firework_sum % 5 == 0:
        created_fireworks["Willow Fireworks"] += 1
    else:
        effect -= 1
        firework_effects.append(effect)
        explosive_power.append(power)
    if created_fireworks["Crossette Fireworks"] >= 3 and created_fireworks["Palm Fireworks"] >= 3 \
            and created_fireworks["Willow Fireworks"] >= 3:
        condition = True
        break
if condition:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in firework_effects)}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_power)}")

for key, count in created_fireworks.items():
    print(f"{key}: {count}")
