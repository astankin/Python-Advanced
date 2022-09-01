def get_max_sum(direction, matrix, row, col):
    sum_of_eggs = 0
    positions = []
    if direction == "up":
        for i in range(row - 1, -1, -1):
            if matrix[i][col] == "X":
                break
            sum_of_eggs += int(matrix[i][col])
            positions.append([i, col])
    elif direction == "down":
        for i in range(row + 1, size, 1):
            if matrix[i][col] == "X":
                break
            sum_of_eggs += int(matrix[i][col])
            positions.append([i, col])
    elif direction == "left":
        for i in range(col - 1, -1, -1):
            if matrix[row][i] == "X":
                break
            sum_of_eggs += int(matrix[row][i])
            positions.append([row, i])
    elif direction == "right":
        for i in range(col + 1, size, 1):
            if matrix[row][i] == "X":
                break
            sum_of_eggs += int(matrix[row][i])
            positions.append([row, i])
    return sum_of_eggs, positions


size = int(input())
matrix = []
bunny_row = 0
bunny_col = 0
directions = ['up', 'down', 'left', 'right']
for row in range(size):
    line = input().split()
    matrix.append(line)
    for col in range(len(line)):
        if line[col] == "B":
            bunny_row = row
            bunny_col = col
best_score = float('-inf')
the_best_direction = ""
best_path = []
for direction in directions:
    max_sum, positions = get_max_sum(direction, matrix, bunny_row, bunny_col)
    if max_sum > best_score and positions:
        best_score = max_sum
        the_best_direction = direction
        best_path = positions

print(the_best_direction)
for row in best_path:
    print(row)
print(best_score)
