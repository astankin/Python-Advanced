def create_matrix():
    matrix_ = []
    for _ in range(6):
        matrix.append(input().split())
    return matrix_


def is_inside(_next_row, _next_col):
    return 0 <= _next_row < 6 and 0 <= _next_col < 6


def moving(direction_, row, col):
    next_row_ = 0
    next_col_ = 0
    if direction_ == "up":
        next_row_ = row - 1
        next_col_ = col
    elif direction_ == "down":
        next_row_ = row + 1
        next_col_ = col
    elif direction_ == "left":
        next_row_ = row
        next_col_ = col - 1
    elif direction_ == "right":
        next_row_ = row
        next_col_ = col + 1
    return next_row_, next_col_


matrix = create_matrix()
position = list(map(int, input().strip("(").strip(")").split(", ")))
player_row = position[0]
player_col = position[1]
while True:
    data = input()
    if data == "Stop":
        break
    command, direction = data.split(", ")[:2]
    next_row, next_col = moving(direction, player_row, player_col)
    if is_inside(next_row, next_col):
        player_row = next_row
        player_col = next_col
    if command == "Create":
        value = data.split(", ")[2]
        if matrix[player_row][player_col] == ".":
            matrix[player_row][player_col] = value
    elif command == "Update":
        value = data.split(", ")[2]
        if matrix[player_row][player_col] != ".":
            matrix[player_row][player_col] = value
    elif command == "Delete":
        if matrix[player_row][player_col] != ".":
            matrix[player_row][player_col] = "."
    elif command == "Read":
        if matrix[player_row][player_col] != ".":
            print(matrix[player_row][player_col])
for row in matrix:
    print(*row, sep=" ")
