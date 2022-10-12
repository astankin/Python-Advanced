from collections import deque

vowels = deque(input().split())
consonants = input().split()
words = {
    "rose": "rose",
    "tulip": "tulip",
    "lotus": "lotus",
    "daffodil": "daffodil"
}
word_found = False
while vowels and consonants:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()

    for key in words:
        words[key] = words[key].replace(current_consonant, "")
        words[key] = words[key].replace(current_vowel, "")
        if words[key] == "":
            print(f"Word found: {key}")
            word_found = True
            break
    if word_found:
        break


if not word_found:
    print("Cannot find any word!")

if vowels:
    print("Vowels left:", *vowels, sep=" ")
if consonants:
    print("Consonants left:", *consonants, sep=" ")
