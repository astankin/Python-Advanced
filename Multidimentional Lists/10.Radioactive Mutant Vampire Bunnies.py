def is_inside(r,c,n, m):
    return 0 <= r < n and 0 <= c < m


def moving_direction(command, player_row, player_col):
    next_row = 0
    next_col = 0
    if command == "U":
        next_row = player_row - 1
        next_col = player_col
    elif command == "L":
        next_row = player_row
        next_col = player_col - 1
    elif command == "R":
        next_row = player_row
        next_col = player_col + 1
    elif command == "D":
        next_row = player_row + 1
        next_col = player_col
    return next_row, next_col


def bunnies_spread(bunnies, row, col):
    new_bunnies_coordinates = set()
    for coordinates in bunnies:
        b_row, b_col = coordinates
        if is_inside(b_row - 1, b_col, row, col):
            new_bunnies_coordinates.add((b_row - 1, b_col))
        if is_inside(b_row, b_col - 1, row, col):
            new_bunnies_coordinates.add((b_row, b_col - 1))
        if is_inside(b_row, b_col + 1, row, col):
            new_bunnies_coordinates.add((b_row, b_col + 1))
        if is_inside(b_row + 1, b_col, row, col):
            new_bunnies_coordinates.add((b_row + 1, b_col))
    return new_bunnies_coordinates


row, col = [int(x) for x in input().split()]
matrix = []

player_row = 0
player_col = 0
bunnies = set()
dead = False
won = False
for i in range(row):
    line = list(input())
    matrix.append(line)
    for j in range(len(line)):
        if line[j] == "P":
            player_row = i
            player_col = j
        elif line[j] == "B":
            bunnies.add((i, j))
data = input()
for command in data:
    next_row, next_col = moving_direction(command, player_row, player_col)
    if is_inside(next_row, next_col, row, col) and matrix[next_row][next_col] != "B":
        matrix[next_row][next_col] = "P"
        matrix[player_row][player_col] = "."
        player_row = next_row
        player_col = next_col
    elif is_inside(next_row, next_col, row, col) and matrix[next_row][next_col] == "B":
        dead = True
        player_row = next_row
        player_col = next_col
    elif not is_inside(next_row, next_col, row, col):
        won = True
        matrix[player_row][player_col] = "."

    bunnies = bunnies.union(bunnies_spread(bunnies, row, col))
    for bunny in bunnies:
        if matrix[bunny[0]][bunny[1]] == "P":
            dead = True
            matrix[bunny[0]][bunny[1]] = "B"
        else:
            matrix[bunny[0]][bunny[1]] = "B"
    if won:
        break
    if dead:
        break
for row in matrix:
    print(*row, sep="")
if won:
    print(f"won: {player_row} {player_col}")
if dead:
    print(f"dead: {player_row} {player_col}")





