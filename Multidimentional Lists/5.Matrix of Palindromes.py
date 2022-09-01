n, m = [int(x) for x in input().split()]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(n):
    for j in range(m):
        word = letters[i] + letters[j+i] + letters[i]
        print(word, end=" ")
    print()
