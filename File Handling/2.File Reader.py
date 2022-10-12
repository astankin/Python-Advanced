import os

if os.path.exists("numbers.txt"):
    with open("numbers.txt") as file:
        numbers = file.readlines()
        result = 0
        for num in numbers:
            result += int(num)
        print(result)
        print(sum(int(x) for x in numbers))
else:
    print("File not found")
