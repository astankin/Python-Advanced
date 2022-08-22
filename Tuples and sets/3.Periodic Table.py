n = int(input())
result = set()
for _ in range(n):
    data = set(input().split())
    result = result.union(data)

print(*result, sep='\n')
















