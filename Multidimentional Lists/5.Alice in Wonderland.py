def is_inside(row, col, n):
    return 0 > next_row or next_row >= n or 0 > next_col or next_col >= n

n = int(input())
matrix = []
alice_row = 0
alice_col = 0
tea_bags_collected = 0
failed = False
going_to_party = False
for row in range(n):
    line = input().split()
    matrix.append(line)
    for col in range(n):
        if line[col] == "A":
            alice_row = row
            alice_col = col
while True:
    command = input()
    next_row = 0
    next_col = 0
    if command == 'up':
        next_row = alice_row - 1
        next_col = alice_col
    elif command == 'down':
        next_row = alice_row + 1
        next_col = alice_col
    elif command == 'left':
        next_row = alice_row
        next_col = alice_col - 1
    elif command == 'right':
        next_row = alice_row
        next_col = alice_col + 1
    if is_inside(next_row, next_col, n):
        failed = True
        matrix[alice_row][alice_col] = "*"
        break
    if matrix[next_row][next_col].isdigit():
        tea_bags_collected += int(matrix[next_row][next_col])
        matrix[alice_row][alice_col] = "*"
        alice_row = next_row
        alice_col = next_col
        if tea_bags_collected >= 10:
            going_to_party = True
            matrix[next_row][next_col] = "*"
            break
    elif matrix[next_row][next_col] == "R":
        failed = True
        matrix[alice_row][alice_col] = "*"
        matrix[next_row][next_col] = "*"
        break
    else:
        matrix[alice_row][alice_col] = "*"
        alice_row = next_row
        alice_col = next_col

if going_to_party:
    print("She did it! She went to the party.")
if failed:
    print("Alice didn't make it to the tea party.")
for row in matrix:
    print(*row, sep=" ")