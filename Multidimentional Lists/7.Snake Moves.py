rows, cols = [int(x) for x in input().split()]
string = input()

snake = string*rows*cols
for i in range(rows):
    output = snake[:cols]
    if i % 2 == 0:
        print(output)
    else:
        print(output[::-1])
    snake = snake.replace(output, "", 1)
