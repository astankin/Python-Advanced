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
    return 0 <= row < 6 and 0 <= col < 6


matrix = [[line for line in input().split()] for _ in range(6)]
#player_row, player_col = [int(x) for x in input().strip("(").strip(")").split(", ")]
player_row, player_col = eval(input())
while True:
    data = input()
    if data == "Stop":
        break
    command = data.split(", ")[0]
    direction = data.split(", ")[1]
    next_row = 0
    next_col = 0
    if command == "Create":
        value = data.split(", ")[2]
        next_row, next_col = moving(direction, player_row, player_col)
        if is_inside(next_row, next_col) and matrix[next_row][next_col] == ".":
            matrix[next_row][next_col] = value

    elif command == "Update":
        value = data.split(", ")[2]
        next_row, next_col = moving(direction, player_row, player_col)
        if is_inside(next_row, next_col) and matrix[next_row][next_col] != ".":
            matrix[next_row][next_col] = value

    elif command == "Delete":
        next_row, next_col = moving(direction, player_row, player_col)
        if is_inside(next_row, next_col) and matrix[next_row][next_col] != ".":
            matrix[next_row][next_col] = "."

    elif command == "Read":
        next_row, next_col = moving(direction, player_row, player_col)
        if is_inside(next_row, next_col) and matrix[next_row][next_col] != ".":
            print(matrix[next_row][next_col])
    player_row, player_col = next_row, next_col

[print(*row, sep=" ") for row in matrix]
