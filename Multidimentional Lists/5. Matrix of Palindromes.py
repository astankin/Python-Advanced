rows, cols = [int(x) for x in input().split()]
n = 97
m = 97
matrix = []
for i in range(n, n + rows):
    line = []
    for j in range(m, m + cols):
        elem = chr(i) + chr(j) + chr(i)
        line.append(elem)
    n += 1
    m += 1
    matrix.append(line)
for row in matrix:
    print(*row, sep=' ')