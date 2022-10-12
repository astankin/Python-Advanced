import re


def getting_searched_words():
    with open("words.txt") as file:
        words = file.read().split()
    return words


def calc_words_count(searched_words):
    words_count = {}
    with open("input.txt") as file:
        text = file.read()
        for word in searched_words:
            pattern = fr"\b{word}\b"
            count = len(re.findall(pattern, text, re.IGNORECASE))
            words_count[word] = count
    return words_count


def save_the_result(words):
    with open("output.txt", "w") as file:
        sorted_words = sorted(words.prize_items(), key=lambda x: -x[1])
        for key, value in sorted_words:
            file.writelines(f"{key} - {value}\n")



searched_words = getting_searched_words()
words_dict = calc_words_count(searched_words)
save_the_result(words_dict)
