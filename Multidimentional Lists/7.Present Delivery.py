def moving(direction, row, col):
    if direction == "up":
        return row - 1, col
    elif direction == "down":
        return row + 1, col
    elif direction == "left":
        return row, col - 1
    elif direction == "right":
        return row, col + 1


def naughty_or_nice_check(row, col, presents_count, nice_kids_count, matrix):
    if matrix[row][col] == "V":
        presents_count -= 1
        nice_kids_count -= 1
        matrix[row][col] = "-"
    elif matrix[row][col] == "X":
        presents_count -= 1
        matrix[row][col] = "-"
    return presents_count, nice_kids_count


def is_inside(r, c, size):
    return 0 <= r < size and 0 <= c < size


presents_count = int(input())
n = int(input())
matrix = []
santa_row = 0
santa_col = 0
nice_kids_count = 0

no_more_presents = False
for row in range(n):
    line = input().split()
    nice_kids_count += line.count("V")
    matrix.append(line)
    for col in range(n):
        if line[col] == "S":
            santa_row = row
            santa_col = col
count_nice_kids = nice_kids_count
command = input()
while not command == "Christmas morning":
    next_row, next_col = moving(command, santa_row, santa_col)
    if is_inside(next_row, next_col, n) and matrix[next_row][next_col] == "V":
        presents_count -= 1
        nice_kids_count -= 1
    elif is_inside(next_row, next_col, n) and matrix[next_row][next_col] == "C":
        presents_count, nice_kids_count = naughty_or_nice_check(next_row - 1, next_col, presents_count, nice_kids_count, matrix)
        presents_count, nice_kids_count = naughty_or_nice_check(next_row + 1, next_col, presents_count, nice_kids_count, matrix)
        presents_count, nice_kids_count = naughty_or_nice_check(next_row, next_col - 1, presents_count, nice_kids_count, matrix)
        presents_count, nice_kids_count = naughty_or_nice_check(next_row, next_col + 1, presents_count, nice_kids_count, matrix)
    matrix[santa_row][santa_col] = "-"
    matrix[next_row][next_col] = "S"
    santa_row = next_row
    santa_col = next_col
    if presents_count == 0:
        no_more_presents = True
        break
    command = input()
if no_more_presents and nice_kids_count > 0:
    print(f"Santa ran out of presents!")
for row in matrix:
    print(*row, sep=" ")
if nice_kids_count <= 0:
    print(f"Good job, Santa! {count_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_count} nice kid/s.")