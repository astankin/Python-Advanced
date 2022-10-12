from collections import deque


def moving(direction, row, col):
    if direction == "up":
        row -= 1
    elif direction == "down":
        row += 1
    elif direction == "left":
        col -= 1
    elif direction == "right":
        col += 1
    return row, col


def get_new_position(row, col):
    if row < 0:
        row = 5
    if col < 0:
        col = 5
    if row == 6:
        row = 0
    if col == 6:
        col = 0
    return row, col


def is_inside(row, col):
    return 0 <= row < 6 and 0 <= col < 6


matrix = []
rover_row = 0
rover_col = 0
deposits = {
    "W": "Water",
    "M": "Metal",
    "C": "Concrete"
}

deposits_found = {"W": 0, "M": 0, "C": 0}
for row in range(6):
    line = input().split()
    matrix.append(line)
    if "E" in line:
        rover_row = row
        rover_col = line.index("E")
commands = deque(input().split(", "))
while commands:
    command = commands.popleft()
    next_row, next_col = moving(command, rover_row, rover_col)
    if not is_inside(next_row, next_col):
        next_row, next_col = get_new_position(next_row, next_col)
    if matrix[next_row][next_col] in deposits:
        deposits_found[matrix[next_row][next_col]] += 1
        print(f"{deposits[matrix[next_row][next_col]]} deposit found at ({next_row}, {next_col})")
    elif matrix[next_row][next_col] == "R":
        print(f"Rover got broken at ({next_row}, {next_col})")
        break
    rover_row, rover_col = next_row, next_col

if 0 in deposits_found.values():
    print("Area not suitable to start the colony.")
else:
    print("Area suitable to start the colony.")
