def create_matrix():
    matrix = [['-' for _ in range(3)] for _ in range(3)]
    return matrix


def insert_symbol(matrix, row, column, symbol):
    matrix[row][column] = symbol
    return matrix

matrix = create_matrix()
[print(' '.join(row)) for row in matrix]

for _ in range(9):
    row, column = [int(x) for x in input("Виведете координати: ").split(", ")]
    symbol = input("Въведете символ: ")
    matrix = insert_symbol(matrix, row, column, symbol)
    [print(' '.join(row)) for row in matrix]
