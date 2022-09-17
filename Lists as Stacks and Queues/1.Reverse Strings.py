string = list(input())
stack = []
for i in range(len(string)):
    stack.append(string.pop())
print(*stack, sep="")
