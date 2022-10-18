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


n = int(input())
matrix = []
snake_row = 0
snake_col = 0
burrow_coordinates = []
food_quantity = 0

for i in range(n):
    line = list(input())
    matrix.append(line)
    for j in range(n):
        if line[j] == "S":
            snake_row = i
            snake_col = j
        if line[j] == "B":
            burrow_coordinates.append((i, j))

while True:
    command = input()
    if not command:
        break
    next_row, next_col = moving(command, snake_row, snake_col)
    matrix[snake_row][snake_col] = "."
    if is_inside(next_row, next_col, n):
        if matrix[next_row][next_col] == "*":
            food_quantity += 1
            snake_row, snake_col = next_row, next_col
            matrix[snake_row][snake_col] = "S"
        elif matrix[next_row][next_col] == "B":
            matrix[next_row][next_col] = "."
            if (next_row, next_col) == burrow_coordinates[0]:
                snake_row, snake_col = burrow_coordinates[1]
            elif (next_row, next_col) == burrow_coordinates[1]:
                snake_row, snake_col = burrow_coordinates[0]
            matrix[snake_row][snake_col] = "S"
        else:
            snake_row, snake_col = next_row, next_col
            matrix[snake_row][snake_col] = "S"

    else:
        print("Game over!")
        break
    if food_quantity >= 10:
        print("You won! You fed the snake.")
        break

print(f"Food eaten: {food_quantity}")

for row in matrix:
    print(*row, sep="")
    