n = int(input())
odd = set()
even = set()
for i in range(1, n + 1):
    name = input()
    result = sum([ord(ch) for ch in name]) // i
    if result % 2 == 0:
        even.add(result)
    else:
        odd.add(result)
even_sum = sum(even)
odd_sum = sum(odd)
if even_sum == odd_sum:
    print(', '.join(str(el) for el in even.union(odd)))
elif odd_sum > even_sum:
    print(*odd.difference(even), sep=", ")
elif odd_sum < even_sum:
    print(*odd.symmetric_difference(even), sep=", ")