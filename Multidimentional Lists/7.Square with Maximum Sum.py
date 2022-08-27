n, m = [int(x) for x in input().split(', ')]
matrix = []
biggest_sum = 0
biggest_submatrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split(', ')])

for i in range(n - 1):
    for j in range(m - 1):
        sub_matrix = [matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]]
        if sum(sub_matrix) > biggest_sum:
            biggest_sum = sum(sub_matrix)
            biggest_submatrix = sub_matrix

print(biggest_submatrix[0], biggest_submatrix[1])
print(biggest_submatrix[2], biggest_submatrix[3])
print(biggest_sum)
