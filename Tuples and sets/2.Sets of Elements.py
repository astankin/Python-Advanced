n, m = list(map(int, input().split()))
first_set = set()
second_set = set()
result = ""
for _ in range(n):
    num = int(input())
    first_set.add(num)
for _ in range(m):
    num = int(input())
    second_set.add(num)
result = first_set.intersection(second_set)

print(*result, sep="\n")