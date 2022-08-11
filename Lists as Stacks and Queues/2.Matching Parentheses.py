text = input()
collection = []
for i in range(len(text)):
    if text[i] == "(":
        collection.append(i)
    elif text[i] == ")":
        start_index = collection.pop()
        print(text[start_index: i + 1])
