def adding_numbers(sequence):
    nums = set([int(num) for num in command[2:]])
    sequence = sequence.union(nums)
    return sequence


def removing_numbers(sequence):
    nums = set([int(num) for num in command if num.isdigit()])
    sequence = sequence.difference(nums)
    return sequence


first_sequence = set([int(num) for num in input().split()])
second_sequence = set([int(num) for num in input().split()])
n = int(input())
for _ in range(n):
    command = input().split()
    if command[0] == "Add":
        if command[1] == "First":
            first_sequence = adding_numbers(first_sequence)
        elif command[1] == "Second":
            second_sequence = adding_numbers(second_sequence)
    elif command[0] == "Remove":
        if command[1] == "First":
            first_sequence = removing_numbers(first_sequence)
        elif command[1] == "Second":
            second_sequence = removing_numbers(second_sequence)
    elif command[0] == "Check":
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence)) # Printing True or False 

print(*sorted(first_sequence), sep=', ')
print(*sorted(second_sequence), sep=', ')
