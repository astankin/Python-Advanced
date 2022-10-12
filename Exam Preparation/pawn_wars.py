def is_inside(row_, col_):
    return 0 <= row_ < 8 and 0 <= col_ < 8


row = {0: "8", 1: "7", 2: "6", 3: "5", 4: "4", 5: "3", 6: "2", 7: "1"}
col = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}

matrix = []
white_row = 0
white_col = 0
black_row = 0
black_col = 0
for i in range(8):
    line = input().split()
    matrix.append(line)
    if "w" in line:
        white_row = i
        white_col = line.index("w")
    if "b" in line:
        black_row = i
        black_col = line.index("b")

while True:

    if is_inside(white_row - 1, white_col - 1) and matrix[white_row - 1][white_col - 1] == 'b':
        print(f"Game over! White win, capture on {col[black_col]}{row[black_row]}.")
        break
    elif matrix[white_row - 1][white_col + 1] == 'b' and is_inside(white_row - 1, white_col + 1):
        print(f"Game over! White win, capture on {col[black_col]}{row[black_row]}.")
        break

    matrix[white_row][white_col] = "-"
    white_row -= 1
    matrix[white_row][white_col] = "w"

    if white_row == 0:
        print(f"Game over! White pawn is promoted to a queen at {col[white_col]}{row[0]}.")
        break

    if matrix[black_row + 1][black_col - 1] == 'w' and is_inside(black_row + 1, black_col - 1):
        print(f"Game over! Black win, capture on {col[white_col]}{row[white_row]}.")
        break
    elif matrix[black_row + 1][black_col + 1] == 'w' and is_inside(black_row + 1, black_col + 1):
        print(f"Game over! Black win, capture on {col[white_col]}{row[white_row]}.")
        break

    matrix[black_row][black_col] = "-"
    black_row += 1
    matrix[black_row][black_col] = "b"

    if black_row == 7:
        print(f"Game over! Black pawn is promoted to a queen at {col[black_col]}{row[7]}.")
        break
