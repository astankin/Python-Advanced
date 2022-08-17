class Stack:
    def __init__(self):
        self.values = []

    def push(self, elem):
        return self.values.append(elem)

    def pop(self):
        return self.values.pop()

    def peek(self):
        return self.values[-1]

    def count(self):
        return len(self.values)


# stack = Stack()
#
# text = [11, 42, 32, 54, 25, 6, 74]
# for el in text:
#     stack.push(el)
# print(stack.pop())
