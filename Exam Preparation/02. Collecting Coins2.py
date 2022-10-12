def get_new_position(direction, row, col, size):
    def moving_to_the_opposite_side(r, c, s):
        if r >= s:
            r = 0
        if r < 0:
            r = s - 1
        if c >= s:
            c = 0
        if c < 0:
            c = s - 1
        return r, c
    if direction == "up":
        row -= 1
    elif direction == "down":
        row += 1
    elif direction == "left":
        col -= 1
    elif direction == "right":
        col += 1
    if 0 <= row < size and 0 <= col < size:
        return row, col
    else:
        return moving_to_the_opposite_side(row, col, size)


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
    next_row, next_col = get_new_position(command, player_row, player_col, n)
    matrix[player_row][player_col] = "0"
    player_row, player_col = next_row, next_col
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
