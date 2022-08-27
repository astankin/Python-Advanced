def create_matrix(n):
    matrix = []
    for _ in range(n):
        matrix.append([int(x) for x in input().split()])
    return matrix


def diagonal_sum_calc(matrix):
    diagonal_sum = 0
    for i in range(n):
        diagonal_sum += matrix[i][i]
    return diagonal_sum


n = int(input())
matrix = create_matrix(n)
print(diagonal_sum_calc(matrix))
