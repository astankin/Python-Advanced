def moving_lef(row, col, matrix):
    while col > 0:
        col -= 1
        if matrix[row][col] == "Q":
            queen_coordinates.append([row, col])
            break


def moving_right(row, col, matrix):
    while col < 7:
        col += 1
        if matrix[row][col] == "Q":
            queen_coordinates.append([row, col])
            break


def moving_up(row, col, matrix):
    while row > 0:
        row -= 1
        if matrix[row][col] == "Q":
            queen_coordinates.append([row, col])
            break


def moving_down(row, col, matrix):
    while row < 7:
        row += 1
        if matrix[row][col] == "Q":
            queen_coordinates.append([row, col])
            break


def moving_left_diagonal(row, col, matrix):
    while row > 0 and col > 0:
        row -= 1
        col -= 1
        if matrix[row][col] == "Q":
            queen_coordinates.append([row, col])
            break
    while row < 7 and col < 7:
        row += 1
        col += 1
        if matrix[row][col] == "Q":
            queen_coordinates.append([row, col])
            break


def moving_right_diagonal(row, col, matrix):
    while row > 0 and col < 7:
        row -= 1
        col += 1
        if matrix[row][col] == "Q":
            queen_coordinates.append([row, col])
            break
    while row < 7 and col > 0:
        row += 1
        col -= 1
        if matrix[row][col] == "Q":
            queen_coordinates.append([row, col])
            break


matrix = []
king_row = 0
king_col = 0
queen_coordinates = []
for i in range(8):
    line = input().split()
    matrix.append(line)
    if "K" in line:
        king_row = i
        king_col = line.index("K")

moving_lef(king_row, king_col, matrix)
moving_right(king_row, king_col, matrix)
moving_up(king_row, king_col, matrix)
moving_down(king_row, king_col, matrix)
moving_left_diagonal(king_row, king_col, matrix)
moving_right_diagonal(king_row, king_col, matrix)

if queen_coordinates:
    print(*queen_coordinates, sep='\n')
else:
    print("The king is safe!")
