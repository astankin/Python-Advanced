def moving(direction, a_row, a_col):
    if direction == "up":
        a_row -= 1
    elif direction == "down":
        a_row += 1
    elif direction == "left":
        a_col -= 1
    elif direction == "right":
        a_col += 1
    return a_row, a_col


def is_inside_the_field(r, c, n):
    return 0 <= r < n and 0 <= c < n


n = int(input())
matrix = []
alice_row = 0
alice_col = 0
collected_tea_bags = 0
go_to_tea_party = False
for row in range(n):
    line = input().split()
    matrix.append(line)
    if "A" in line:
        alice_row = row
        alice_col = line.index("A")

while True:
    command = input()
    if command == "":
        break
    next_row, next_col = moving(command, alice_row, alice_col)
    if is_inside_the_field(next_row, next_col, n):
        if matrix[next_row][next_col].isdigit():
            matrix[alice_row][alice_col] = "*"
            alice_row = next_row
            alice_col = next_col
            collected_tea_bags += int(matrix[next_row][next_col])
            if collected_tea_bags >= 10:
                matrix[alice_row][alice_col] = "*"
                go_to_tea_party = True
                break
        elif matrix[next_row][next_col] == "R":
            matrix[alice_row][alice_col] = "*"
            matrix[next_row][next_col] = "*"
            break
        else:
            matrix[alice_row][alice_col] = "*"
            alice_row = next_row
            alice_col = next_col

    else:
        matrix[alice_row][alice_col] = "*"
        break
if not go_to_tea_party:
    print(f"Alice didn't make it to the tea party.")
else:
    print(f"She did it! She went to the party.")
[print(*row) for row in matrix]