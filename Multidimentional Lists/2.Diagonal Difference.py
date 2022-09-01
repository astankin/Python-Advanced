def create_matrix(n):
    matrix = []
    for _ in range(n):
        matrix.append([int(x) for x in input().split()])
    return matrix


def get_primary_sum(matrix):
    primary_sum = 0
    for i in range(len(matrix)):
        primary_sum += matrix[i][i]
    return primary_sum


def get_secondary_sum(matrix):
    secondary_sum = 0
    for i in range(len(matrix)):
        secondary_sum += matrix[i][n-1-i]
    return secondary_sum

n = int(input())

matrix = create_matrix(n)
result = abs(get_primary_sum(matrix) - get_secondary_sum(matrix))
print(result)