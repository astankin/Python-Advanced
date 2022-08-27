from collections import deque

string = deque(input().split())
main_colours = ['red', 'yellow', 'blue']
second_colours = ['orange', 'purple', 'green']
collected_colours = []
while string:
    left = string.popleft()
    right = string.pop() if string else ""

    result = left + right
    if result in main_colours or result in second_colours:
        collected_colours.append(result)
        continue
    result = right + left
    if result in main_colours or result in second_colours:
        collected_colours.append(result)
        continue
    left = left[:-1]
    right = right[:-1]
    string.insert(len(string)//2, left) if left else None
    if right:
        string.insert(len(string)//2, right)
result = []
ingredients = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue']
}

for colour in collected_colours:
    if colour in main_colours:
        result.append(colour)
        continue
    is_collected = True
    for ingredient in ingredients[colour]:
        if ingredient not in collected_colours:
            is_collected = False
            break
    if is_collected:
        result.append(colour)

print(result)
