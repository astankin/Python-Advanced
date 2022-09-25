def is_inside(row, col, n):
    return 0 <= row < n and 0 <= col < n


def moving(direction, b_row, b_col):
    if direction == "up":
        b_row -= 1
    elif direction == "down":
        b_row += 1
    elif direction == "left":
        b_col -= 1
    elif direction == "right":
        b_col += 1
    return b_row, b_col


n = int(input())
matrix = []
directions = ["up", "down", "left", "right"]
bunny_row = 0
bunny_col = 0
for i in range(n):
    line = input().split()
    matrix.append(line)
    if "B" in line:
        bunny_row = i
        bunny_col = line.index("B")

the_best_direction = ""
the_best_coordinates = []
the_best_sum = float('-inf')
for direction in directions:
    b_row = bunny_row
    b_col = bunny_col
    coordinates = []
    collected_eggs = 0
    while True:
        next_row, next_col = moving(direction, b_row, b_col)
        if is_inside(next_row, next_col, n) and matrix[next_row][next_col] != "X":
            collected_eggs += int(matrix[next_row][next_col])
            coordinates.append([next_row, next_col])
            b_row = next_row
            b_col = next_col
        else:
            break
    if collected_eggs > the_best_sum and coordinates:
        the_best_sum = collected_eggs
        the_best_direction = direction
        the_best_coordinates = coordinates
print(the_best_direction)
for elem in the_best_coordinates:
    print(f"{elem}")
print(the_best_sum)
