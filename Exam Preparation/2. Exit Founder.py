from collections import deque

player_names = deque(input().split(", "))
matrix = []
for _ in range(6):
    matrix.append(input().split())


players_need_rest = []
while True:
    command = input()
    if command == "":
        break
    player_row, player_col = [int(x) for x in command.strip("(").strip(")").split(", ")]

    player = player_names.popleft()

    if player in players_need_rest:
        players_need_rest.remove(player)
        player_names.append(player)
        continue
    if matrix[player_row][player_col] == "E":
        print(f"{player} found the Exit and wins the game!")
        break
    elif matrix[player_row][player_col] == "T":
        print(f"{player} is out of the game! The winner is {''.join(player_names)}.")
        break
    elif matrix[player_row][player_col] == "W":
        print(f"{player} hits a wall and needs to rest.")
        players_need_rest.append(player)

    player_names.append(player)



