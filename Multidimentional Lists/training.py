def moving(direct, row, col, steps):
    if direct == "right":
        col += steps
    elif direct == "left":
        col -= steps
    elif direct == "up":
        row -= steps
    elif direct == "down":
        row += steps
    return row, col


def is_inside(row, col):
    return 0 <= row < 5 and 0 <= col < 5


def shooting(direct, row, col):
    shot_targets = 0
    targets_coordinates = []
    while True:
        if direct == "down":
            row += 1
        elif direct == "up":
            row -= 1
        elif direct == "left":
            col -= 1
        elif direct == "right":
            col += 1
        if not is_inside(row, col):
            break
        if matrix[row][col] == "x":
            matrix[row][col] = "."
            shot_targets = 1
            targets_coordinates.append([row, col])
            break
    return shot_targets, targets_coordinates


matrix = []
player_row = 0
player_col = 0
targets_count = 0
for i in range(5):
    line = input().split()
    matrix.append(line)
    if "A" in line:
        player_row = i
        player_col = line.index("A")
    if "x" in line:
        targets_count += line.count("x")

number_of_commands = int(input())
total_targets_shot = 0
targets = []
for _ in range(number_of_commands):
    command = input().split()
    direction = command[1]
    if command[0] == "move":
        steps = int(command[2])
        next_row, next_col = moving(direction, player_row, player_col, steps)
        if is_inside(next_row, next_col) and matrix[next_row][next_col] == ".":
            matrix[player_row][player_col] = "."
            player_row, player_col = next_row, next_col
            matrix[player_row][player_col] = "A"
    elif command[0] == "shoot":
        shot_targets, target_positions = shooting(direction, player_row, player_col)
        total_targets_shot += shot_targets
        targets.extend(target_positions)
        if total_targets_shot == targets_count:
            print(f"Training completed! All {targets_count} targets hit.")
            break

if targets_count - total_targets_shot > 0:
    print(f"Training not completed! {targets_count - total_targets_shot} targets left.")
[print(row) for row in targets]
