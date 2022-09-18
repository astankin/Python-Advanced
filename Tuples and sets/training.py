n = int(input())
row = 0
even_set, odd_set = set(), set()
for i in range(1, n + 1):
    name = input()
    result = sum([ord(el) for el in name]) // row
    if result % 2 == 0:
        even_set.add(result)
    else:
        odd_set.add(result)
if sum(odd_set) == sum(even_set):
    union_set = even_set.union(odd_set)
    print(*union_set, sep=', ')
elif sum(odd_set) > sum(even_set):
    different = odd_set.difference(even_set)
    print(*different, sep=', ')
else:
    sim_diff = odd_set.symmetric_difference(even_set)
    print(*sim_diff, sep=', ')