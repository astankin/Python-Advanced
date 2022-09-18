def add_elements(sequence, data_):
    nums = set(int(x) for x in data_[2:])
    return sequence.union(nums)


def removing_elements(sequence, data_):
    nums = set(int(x) for x in data_[2:])
    return sequence.difference(nums)


first_sequence = set([int(x) for x in input().split()])
second_sequence = set([int(x) for x in input().split()])
n = int(input())

for _ in range(n):
    data = input().split()
    command = data[0]
    if command == "Add":
        if data[1] == "First":
            first_sequence = add_elements(first_sequence, data)
        elif data[1] == "Second":
            second_sequence = add_elements(second_sequence, data)
    elif command == "Remove":
        if data[1] == "First":
            first_sequence = removing_elements(first_sequence, data)
        elif data[1] == "Second":
            second_sequence = removing_elements(second_sequence, data)
    else:
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))
print(*sorted(first_sequence), sep=', ')
print(*sorted(second_sequence), sep=', ')
