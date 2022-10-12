def is_inside(row, col):
    return 0 <= row < 7 and 0 <= col < 7


def calc_score(row, col, times):
    num1 = int(matrix[0][col])
    num2 = int(matrix[6][col])
    num3 = int(matrix[row][0])
    num4 = int(matrix[row][6])
    return (num1 + num2 + num3 + num4) * times


player1, player2 = input().split(", ")
matrix = []
trows = {player1: 0, player2: 0}
players = {player1: 501, player2: 501}
for _ in range(7):
    matrix.append(input().split())
counter = 0
player = ""
while True:
    coordinates = input()
    if not coordinates:
        break
    counter += 1
    trow_row, trow_col = [int(x) for x in coordinates.strip("(").strip(")").split(", ")]
    player = player1
    if counter % 2 == 0:
        player = player2
    trows[player] += 1
    if not is_inside(trow_row, trow_col):
        continue
    if matrix[trow_row][trow_col] == "B":
        break
    elif matrix[trow_row][trow_col] == "D":
        players[player] -= calc_score(trow_row, trow_col, 2)
    elif matrix[trow_row][trow_col] == "T":
        players[player] -= calc_score(trow_row, trow_col, 3)
    if matrix[trow_row][trow_col].isdigit():
        players[player] -= int(matrix[trow_row][trow_col])
    if players[player] <= 0:
        break


print(f"{player} won the game with {trows[player]} throws!")
