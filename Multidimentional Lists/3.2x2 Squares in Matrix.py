def create_matrix(n):
    matrix = []
    for _ in range(n):
        matrix.append(input().split())
    return matrix


def get_square_matrices(matrix, n, m):
    count = 0
    for i in range(n - 1):
        for j in range(m - 1):
            if matrix[i][j] == matrix[i][j+1] and matrix[i][j] == matrix[i+1][j] and matrix[i+1][j] == matrix[i+1][j+1]:
                count += 1
    return count


n, m = [int(x) for x in input().split()]
matrix = create_matrix(n)
count = get_square_matrices(matrix, n, m)

print(count)
