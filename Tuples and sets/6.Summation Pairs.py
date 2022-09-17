numbers = list(map(int, input().split()))
target = int(input())
counter = 0
unique_pairs = set()
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        counter += 1
        if numbers[i] + numbers[j] == target:
            unique_pairs.add((numbers[i], numbers[j]))
            print(f"{numbers[i]} + {numbers[j]} = {target}")
print(f"Iterations done: {counter}")
[print(pair) for pair in unique_pairs]
print(*unique_pairs, sep='\n')
