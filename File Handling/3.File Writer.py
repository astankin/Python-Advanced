with open("my_first_file.txt", "a") as file:
    file.writelines("I just created my first file!\n")

with open("my_first_file.txt") as file:
    print(file.read())
