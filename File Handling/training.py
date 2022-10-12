

with open("text.txt", "r+") as file:
    text = file.readlines()
    new_content = ""
    for row in range(len(text)):
        new_content += text[row].strip().replace("quick", "fast") + '\n'

with open("text.txt", "w") as file:
    file.write(new_content)
