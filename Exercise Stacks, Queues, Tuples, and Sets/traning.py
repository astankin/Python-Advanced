from collections import deque

main_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]
ingredients = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue']
}
string = deque(input().split())
fined_colors = []
while string:
    left_part = string.popleft()
    right_part = string.pop() if string else ""
    if left_part + right_part in main_colors or left_part + right_part in secondary_colors:
        fined_colors.append(left_part + right_part)
    elif right_part + left_part in main_colors or right_part + left_part in secondary_colors:
        fined_colors.append(right_part + left_part)
    else:
        left_part = left_part[:-1]
        right_part = right_part[:-1]
        if left_part:
            string.insert(len(string) // 2, left_part)
        if right_part:
            string.insert(len(string) // 2, right_part)


for color in fined_colors:
    if color in secondary_colors:
        for ingredient in ingredients[color]:
            if ingredient not in fined_colors:
                fined_colors.remove(color)
print(fined_colors)