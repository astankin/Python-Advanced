import sys


def create_matrix(n):
    matrix = []
    for _ in range(n):
        matrix.append([int(x) for x in input().split()])
    return matrix


def get_max_sum(matrix, n, m):
    max_sum = -sys.maxsize
    sub_matrix = []
    for i in range(n - 2):
        for j in range(m - 2):
            current_sum = matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2] + \
                          matrix[i + 1][j] + matrix[i + 1][j + 1] + matrix[i + 1][j + 2] + \
                          matrix[i + 2][j] + matrix[i + 2][j + 1] + matrix[i + 2][j + 2]
            if current_sum > max_sum:
                max_sum = current_sum
                sub_matrix = [matrix[i][j], matrix[i][j + 1], matrix[i][j + 2],
                              matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2],
                              matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]]

    return max_sum, sub_matrix


n, m = [int(x) for x in input().split()]
matrix = create_matrix(n)
max_sum, sub_matrix = get_max_sum(matrix, n, m)
print(f"Sum = {max_sum}")
print(sub_matrix[0], sub_matrix[1], sub_matrix[2])
print(sub_matrix[3], sub_matrix[4], sub_matrix[5])
print(sub_matrix[6], sub_matrix[7], sub_matrix[8])
