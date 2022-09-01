n, m = [int(x) for x in input().split()]
text = input()
matrix = []
idx = 0
for i in range(n):
    row = ""
    for col in range(m):
        row += text[idx % len(text)]
        idx += 1
    if i % 2 == 0:
        matrix.append(row)
    else:
        matrix.append(row[::-1])
for row in matrix:
    print(*row, sep="")
