def create_matrix(n):
    return [[x for x in input().split()] for _ in range(n)]


def print_matrix(matrix):
    for row in matrix:
        print(*row, sep=" ")


def index_validation(n, m, row1, col1, row2, col2):
    return row1 in range(n) and col1 in range(m) and row2 in range(n) and col2 in range(m)


n, m = [int(x) for x in input().split()]
matrix = create_matrix(n)

data = input()
while not data == "END":
    data = data.split()
    command = data[0]
    if command == "swap" and len(data) == 5:
        row1, col1, row2, col2 = [int(x) for x in data[1:]]
        if index_validation(n, m, row1, col1, row2, col2):
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            print_matrix(matrix)
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
    data = input()