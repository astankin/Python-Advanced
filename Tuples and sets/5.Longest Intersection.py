n = int(input())
longest_intersection = set()
for _ in range(n):
    first, second = input().split("-")
    first_start = int(first.split(",")[0])
    first_end = int(first.split(",")[1])
    second_start = int(second.split(",")[0])
    second_end = int(second.split(",")[1])
    set1 = set([num for num in range(first_start, first_end+1)])
    set2 = set([num for num in range(second_start, second_end+1)])
    result = set1.intersection(set2)
    if len(result) > len(longest_intersection):
        longest_intersection = result
print(f"Longest intersection is [{', '.join(str(num) for num in longest_intersection)}] with length {len(longest_intersection)}")