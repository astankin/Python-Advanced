def move(direction, row, col, steps):
    if direction == "up":
        return row - steps, col
    elif direction == "down":
        return player_row + steps, col
    elif direction == "left":
        return row, col - steps
    elif direction == "right":
        return row, col + steps


def shooting(direction, player_row, player_col, matrix):
    shot_targets = 0
    targets_positions = []
    if direction == "up":
        for row in range(player_row - 1, -1, -1):
            target_row = row
            target_col = player_col
            if matrix[target_row][target_col] == "x":
                shot_targets += 1
                targets_positions.append(target_row)
                targets_positions.append(target_col)
                matrix[target_row][target_col] = "."
                break

    elif direction == "down":
        for row in range(player_row + 1, 5, 1):
            target_row = row
            target_col = player_col
            if matrix[target_row][target_col] == "x":
                shot_targets += 1
                targets_positions.append(target_row)
                targets_positions.append(target_col)
                matrix[target_row][target_col] = "."
                break

    elif direction == "left":
        for col in range(player_col - 1, -1, -1):
            target_row = player_row
            target_col = col
            if matrix[target_row][target_col] == "x":
                shot_targets += 1
                targets_positions.append(target_row)
                targets_positions.append(target_col)
                matrix[target_row][target_col] = "."
                break
    elif direction == "right":
        for col in range(player_col + 1, 5, 1):
            target_row = player_row
            target_col = col
            if matrix[target_row][target_col] == "x":
                shot_targets += 1
                targets_positions.append(target_row)
                targets_positions.append(target_col)
                matrix[target_row][target_col] = "."
                break
    return shot_targets, targets_positions


def is_inside(row, col):
    return 0 <= row < 5 and 0 <= col < 5


matrix = []
player_row = 0
player_col = 0
targets_count = 0
for i in range(5):
    line = input().split()
    matrix.append(line)
    targets_count += line.count("x")
    for j in range(len(line)):
        if line[j] == "A":
            player_row = i
            player_col = j
number_of_commands = int(input())
total_shot_targets = 0
shot_targets_positions = []
for _ in range(number_of_commands):
    data = input().split()
    command = data[0]
    direction = data[1]
    if command == "move":
        steps = int(data[2])
        new_row, new_col = move(direction, player_row, player_col, steps)
        if is_inside(new_row, new_col) and matrix[new_row][new_col] == ".":
            matrix[player_row][player_col] = "."
            player_row = new_row
            player_col = new_col
            matrix[player_row][player_col] = "A"

    elif command == "shoot":
        shot_targets, target_positions = shooting(direction, player_row, player_col, matrix)
        total_shot_targets += shot_targets
        if target_positions:
            shot_targets_positions.append(target_positions)
        if total_shot_targets == targets_count:
            print(f"Training completed! All {targets_count} targets hit.")
            break
if targets_count - total_shot_targets > 0:
    print(f"Training not completed! {targets_count - total_shot_targets} targets left.")
for row in shot_targets_positions:
    print(row)
