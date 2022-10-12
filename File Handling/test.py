import os


file = open("text.txt")
absolute_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # дава ни пътят на главната директория. Всяко исползване на os.path.dirname излиза една директория нагоре.
file_path = os.path.join(absolute_path, "Example", "test_text.txt")
test = open(file_path)
print(test.read())
print(file.read())

import json

with open("test.json") as json_file:
    my_dict = json.load(json_file)
    print(my_dict)

with open("my_first_file.txt", "a") as file:
    file.writelines("\nI've just created my second line")
with open("my_first_file.txt") as file:
    print(file.read())
