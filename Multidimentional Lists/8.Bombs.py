def create_matrix(n):
    matrix = []
    for _ in range(n):
        matrix.append([int(x) for x in input().split()])
    return matrix


def sum_calc(mat):
    mat_sum = 0
    count = 0
    for row in mat:
        for el in row:
            if el > 0:
                mat_sum += el
                count += 1
    return mat_sum, count


def get_neighborhood(n, m):
    neighborhood = []
    for i in range(n-1, n+2):
        for j in range(m-1, m+2):
            if i in range(len(matrix)) and j in range(len(matrix)):
                neighborhood.append((i, j))
    return neighborhood


n = int(input())
matrix = create_matrix(n)
coordinates = input().split()

for coordinate in coordinates:
    row, col = [int(x) for x in coordinate.split(",")]
    neighborhood = get_neighborhood(row, col)
    if matrix[row][col] > 0:
        damage = matrix[row][col]
        for cell in neighborhood:
            r, c = cell
            if matrix[r][c] > 0:
                matrix[r][c] = matrix[r][c] - damage

sum_of_cells, alive_cells = sum_calc(matrix)
print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_of_cells}")
for row in matrix:
    print(*row, sep=" ")
