numbers = list(map(int, input().split()))
indexes = []
output = []
target = int(input())
for i in range(len(numbers)):
    number = numbers[i]
    for j in range(i + 1, len(numbers)):
        num = numbers[j]
        if number + num == target:
            if i not in indexes and j not in indexes:
                indexes.append(i)
                indexes.append(j)
                print(f"{number} + {num} = {target}")

