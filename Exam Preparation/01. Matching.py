from collections import deque

males = list(map(int, input().split()))
females = deque(map(int, input().split()))
matches = 0
while males and females:
    current_male = males.pop()
    if current_male <= 0:
        continue
    if current_male % 25 == 0:
        males.pop()
        continue
    current_female = females.popleft()
    if current_female % 25 == 0:
        females.popleft()
        males.append(current_male)
        continue
    if current_female <= 0:
        males.append(current_male)
        continue
    if current_female == current_male:
        matches += 1
    else:
        current_male -= 2
        males.append(current_male)

print(f"Matches: {matches}")
if not males:
    print("Males left: none")
else:
    print(f"Males left: {', '.join(map(str, males[::-1]))}")
if not females:
    print("Females left: none")
else:
    print(f"Females left: {', '.join(map(str, females))}")
