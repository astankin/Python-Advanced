def moving(direction, row, col):
    if direction == "up":
        row -= 1
    elif direction == "down":
        row += 1
    elif direction == "left":
        col -= 1
    elif direction == "right":
        col += 1
    return row, col


def is_inside(row, col):
    return 0 <= row < n and 0 <= col < m


def get_new_position(row, col):
    if row < 0:
        row = n - 1
    if col < 0:
        col = m - 1
    if row >= n:
        row = 0
    if col >= m:
        col = 0
    return row, col


n, m = [int(x) for x in input().split(", ")]
matrix = []

collected_items = {"D": 0, "G": 0, "C": 0}
player_row = 0
player_col = 0
items = 0
total_collected_items = 0
for i in range(n):
    line = input().split()
    matrix.append(line)
    if "Y" in line:
        player_row = i
        player_col = line.index("Y")
    if "D" in line:
        items += line.count("D")
    if "G" in line:
        items += line.count("G")
    if "C" in line:
        items += line.count("C")

are_all_items_collected = False
while True:
    if are_all_items_collected:
        break
    command = input()
    if not command:
        break
    if command == "End":
        break

    direction, steps = command.split("-")
    steps = int(steps)
    for step in range(steps):
        next_player_row, next_player_col = moving(direction, player_row, player_col)
        matrix[player_row][player_col] = "x"
        if is_inside(next_player_row, next_player_col):
            player_row, player_col = next_player_row, next_player_col
        else:
            player_row, player_col = get_new_position(next_player_row, next_player_col)
        if matrix[player_row][player_col] in collected_items:
            collected_items[matrix[player_row][player_col]] += 1
            total_collected_items += 1
            if total_collected_items == items:
                matrix[player_row][player_col] = "Y"
                are_all_items_collected = True
                break
        matrix[player_row][player_col] = "Y"

if are_all_items_collected:
    print("Merry Christmas!")
print("You've collected:")
print(f"- {collected_items['D']} Christmas decorations")
print(f"- {collected_items['G']} Gifts")
print(f"- {collected_items['C']} Cookies")
[print(*row) for row in matrix]
