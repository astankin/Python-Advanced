from string import punctuation

with open("text.txt") as input_file, open("output.txt", "w") as output_file:
    line = input_file.readlines()
    for row in range(len(line)):
        letters_count = len([char for char in line[row] if char.isalpha()])
        punctuation_marks = len([char for char in line[row] if char in punctuation])
        output_file.writelines(f"Line {row + 1}: {line[row].strip()} ({letters_count})({punctuation_marks})\n")
