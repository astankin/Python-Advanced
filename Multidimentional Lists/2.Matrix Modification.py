n = int(input())

matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])
while True:
    data = input()
    if data == "END":
        break
    command, row, col, value = data.split()
    row = int(row)
    col = int(col)
    value = int(value)
    if row not in range(len(matrix)) or col not in range(len(matrix)):
        print("Invalid coordinates")
        continue
    if command == "Add":
        matrix[row][col] += value
    elif command == "Subtract":
        matrix[row][col] -= value
[print(*row) for row in matrix]
