def create_matrix(row):
    return [[int(x) for x in input().split(', ')] for _ in range(row)]


def get_primary_diagonal(matrix):
    primary_diagonal = []
    for i in range(len(matrix)):
        primary_diagonal.append(matrix[i][i])
    return primary_diagonal


def get_secondary_diagonal(matrix, n):
    second_diagonal = []
    for i in range(n):
        second_diagonal.append(matrix[i][n - i - 1])
    return second_diagonal


n = int(input())
matrix = create_matrix(n)
primary_diagonal = get_primary_diagonal(matrix)
second_diagonal = get_secondary_diagonal(matrix, n)
print(f'Primary diagonal: {", ".join(str(elm) for elm in primary_diagonal)}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join(str(elm) for elm in second_diagonal)}. Sum: {sum(second_diagonal)}')
