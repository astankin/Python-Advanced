n = int(input())
directions = input().split()
matrix = []
current_position = []
number_of_coils = 0
collected_coils = 0
for i in range(n):
    line = input().split()
    if "s" in line:
        index = line.index("s")
        current_position = [i, index]
    if "c" in line:
        number_of_coils += line.count("c")
    matrix.append(line)
for command in directions:
    next_position = []
    if command == "up":
        next_position = [current_position[0] - 1, current_position[1]]
    elif command == "right":
        next_position = [current_position[0], current_position[1] + 1]
    elif command == "left":
        next_position = [current_position[0], current_position[1] - 1]
    elif command == "down":
        next_position = [current_position[0] + 1, current_position[1]]
    if next_position[0] in range(len(matrix)) and next_position[1] in range(len(matrix)):
        current_position = next_position
    if matrix[current_position[0]][current_position[1]] == "c":
        collected_coils += 1
        matrix[current_position[0]][current_position[1]] = "*"
        if collected_coils == number_of_coils:
            print(f"You collected all coal! ({current_position[0]}, {current_position[1]})")
            exit()
    elif matrix[current_position[0]][current_position[1]] == "e":
        print(f"Game over! ({current_position[0]}, {current_position[1]})")
        exit()
print(f"{number_of_coils - collected_coils} pieces of coal left. ({current_position[0]}, {current_position[1]})")