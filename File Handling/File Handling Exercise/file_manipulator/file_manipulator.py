import os

while True:
    line = input()
    if line == "End":
        break
    command = line.split("-")[0]
    file_name = line.split("-")[1]

    if command == "Create":
        open(file_name, "w").close()

    elif command == "Add":
        content = line.split("-")[2]
        with open(file_name, "a") as file:
            file.write(content + '\n')

    elif command == "Replace":
        old_string = line.split("-")[2]
        new_string = line.split("-")[3]
        try:
            with open(file_name, "r+") as file:  # "+" activates read and write methods
                new_content = file.read().replace(old_string, new_string)
                file.seek(0)      # set the cursor at the beginning of the file
                file.truncate()   # truncate the file size, if no argument is given it clears everything from the file
                file.write(new_content)  # write the new content with the replaced strings
        except FileNotFoundError:
            print("An error occurred")

    elif command == "Delete":
        if os.path.exists(file_name):    # an alternative way of "try-except" to check if the file exists
            os.remove(file_name)
        else:
            print("An error occurred")
