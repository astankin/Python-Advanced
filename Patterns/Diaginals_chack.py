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