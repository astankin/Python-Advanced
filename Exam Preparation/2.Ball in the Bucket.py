import sys

prize_items = {
    (100, 199): "Football",
    (200, 299): "Teddy Bear",
    (300, sys.maxsize): "Lego Construction Set"
}

matrix = []
for _ in range(6):
    lene = input().split()
    matrix.append(lene)
score = 0
for _ in range(3):
    trow_row, trow_col = [int(x) for x in input().strip("(").strip(")").split(", ")]
    if 0 <= trow_row < 6 and 0 <= trow_col < 6:
        if matrix[trow_row][trow_col] == "B":
            matrix[trow_row][trow_col] = "X"
            for row in range(6):
                if matrix[row][trow_col].isdigit():
                    score += int(matrix[row][trow_col])


won_item = ""
for range_, item in prize_items.items():
    if range_[0] <= score <= range_[1]:
        won_item = item
        break
if won_item:
    print(f"Good job! You scored {score} points, and you've won {won_item}.")
else:
    needed_points = 100 - score
    print(f"Sorry! You need {needed_points} points more to win a prize.")