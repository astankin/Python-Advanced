def create_matrix(row):
    matrix = []
    matrix_sum = 0
    for _ in range(row):
        line = [int(x) for x in input().split(', ')]
        matrix_sum += sum(line)
        matrix.append(line)
    return matrix, matrix_sum


row, col = [int(x) for x in input().split(', ')]

matrix, matrix_sum = create_matrix(row)

print(matrix_sum)
print(matrix)