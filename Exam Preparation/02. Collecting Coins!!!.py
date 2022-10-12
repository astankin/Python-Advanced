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


def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_new_position(row, col, size):
    if row >= size:
        row = 0
    if row < 0:
        row = size - 1
    if col >= size:
        col = 0
    if col < 0:
        col = size - 1
    return row, col


n = int(input())
matrix = []

player_row = 0
player_col = 0
total_coins = 0
lose = False
directions = ["up", "down", "left", "right"]
for i in range(n):
    line = input().split()
    matrix.append(line)
    if "P" in line:
        player_row = i
        player_col = line.index("P")

path = [[player_row, player_col]]
while True:
    command = input()
    if not command:
        break
    if command not in directions:
        continue
    next_row, next_col = moving(command, player_row, player_col)
    matrix[player_row][player_col] = "0"
    if is_inside(next_row, next_col, n):
        player_row, player_col = next_row, next_col
    else:
        player_row, player_col = get_new_position(next_row, next_col, n)
    if matrix[player_row][player_col].isdigit():
        total_coins += int(matrix[player_row][player_col])
        matrix[player_row][player_col] = "P"
        path.append([player_row, player_col])
        if total_coins >= 100:
            break
    if matrix[player_row][player_col] == "X":
        path.append([player_row, player_col])
        total_coins = total_coins // 2
        lose = True
        break

if total_coins >= 100:
    print(f"You won! You've collected {total_coins} coins.")
if lose:
    print(f"Game over! You've collected {total_coins} coins.")
print("Your path:")

print(*path, sep='\n')
