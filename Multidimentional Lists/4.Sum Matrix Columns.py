def create_matrix(n):
    matrix = []
    for _ in range(n):
        line = [int(x) for x in input().split()]
        matrix.append(line)
    return matrix


row, col = [int(x) for x in input().split(', ')]

matrix = create_matrix(row)

for j in range(col):
    result = 0
    for i in range(row):
        result += matrix[i][j]
    print(result)
