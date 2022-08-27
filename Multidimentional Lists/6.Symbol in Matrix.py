n = int(input())
matrix = []
for _ in range(n):
    matrix.append(input())

symbol = input()

for i in range(n):
    for j in range(n):
        if matrix[i][j] == symbol:
            coordinates = (i, j)
            print(coordinates)
            exit()

print(f"{symbol} does not occur in the matrix")
