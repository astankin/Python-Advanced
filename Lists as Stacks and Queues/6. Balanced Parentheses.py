text = input()
stack = []
balanced = True
for elem in text:
    if elem in '([{':
        stack.append(elem)
    elif not stack:
        balanced = False
        break
    elif elem in ')}]':
        opening_pren = stack.pop()

        if opening_pren == "{" and elem == "}":
            continue
        elif opening_pren == "[" and elem == "]":
            continue
        elif opening_pren == "(" and elem == ")":
            continue
        else:
            balanced = False
            break

if balanced and len(stack) == 0:
    print("YES")
else:
    print("NO")