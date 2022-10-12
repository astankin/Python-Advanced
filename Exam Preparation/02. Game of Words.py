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


string = input()
n = int(input())
matrix = []
player_row = 0
player_col = 0
for i in range(n):
    line = list(input())
    matrix.append(line)
    if "P" in line:
        player_row = i
        player_col = line.index("P")
m = int(input())
for _ in range(m):
    command = input()
    next_row, next_col = moving(command, player_row, player_col)
    if 0 <= next_row < n and 0 <= next_col < n:
        if matrix[next_row][next_col].isalpha():
            string += matrix[next_row][next_col]
        matrix[player_row][player_col] = "-"
        player_row, player_col = next_row, next_col
        matrix[player_row][player_col] = "P"
    else:
        string = string[:-1]
print(string)
[print(*row, sep="") for row in matrix]
