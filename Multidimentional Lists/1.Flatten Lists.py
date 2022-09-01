from collections import deque

matrix = input().split("|")
new_matrix = deque()
for elm in matrix:
    row = elm.split()
    if row:
        new_matrix.appendleft(row)

for row in new_matrix:
    print(*row, end=" ")