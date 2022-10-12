symbols = ("-", ",", ".", "!", "?")
with open("text.txt") as file:
    text = file.readlines()
    for i in range(len(text)):
        if i % 2 == 0:
            reversed_line = text[i].split()[::-1]
            result = ' '.join(reversed_line)
            for symbol in symbols:
                result = result.replace(symbol, '@')
            print(result)