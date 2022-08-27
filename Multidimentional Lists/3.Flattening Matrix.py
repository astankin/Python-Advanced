n = int(input())
matrix = []
for _ in range(n):
    line = [int(x) for x in input().split(', ')]
    matrix.extend(line)
print(matrix)
