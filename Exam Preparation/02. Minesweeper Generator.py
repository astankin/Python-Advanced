def calculation(r, c):
    def is_inside(r, c):
        return 0 <= r < n and 0 <= c < n
    count = 0
    if is_inside(r, c - 1) and matrix[r][c - 1] == "*":
        count += 1
    if is_inside(r, c + 1) and matrix[r][c + 1] == "*":
        count += 1
    if is_inside(r-1, c) and matrix[r - 1][c] == "*":
        count += 1
    if is_inside(r+1, c) and matrix[r + 1][c] == "*":
        count += 1
    if is_inside(r-1, c-1) and matrix[r - 1][c - 1] == "*":
        count += 1
    if is_inside(r-1, c+1) and matrix[r - 1][c + 1] == "*":
        count += 1
    if is_inside(r+1, c-1) and matrix[r + 1][c - 1] == "*":
        count += 1
    if is_inside(r+1, c+1) and matrix[r + 1][c + 1] == "*":
        count += 1

    return count


n = int(input())
bombs_count = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(bombs_count):
    bomb_row, bomb_col = eval(input())
    matrix[bomb_row][bomb_col] = "*"

for row in range(n):
    for col in range(n):
        if matrix[row][col] != "*":
            matrix[row][col] = calculation(row, col)

[print(*row) for row in matrix]