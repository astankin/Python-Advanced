def words_sorting(*args):
    words = {}
    result = ""
    for word in args:
        words[word] = sum([ord(char) for char in word])
    values_sum = sum(words.values())
    if values_sum % 2 != 0:
        sorted_words = sorted(words.items(), key=lambda x: -x[1])
    else:
        sorted_words = sorted(words.items(), key=lambda x: x[0])

    for key, value in sorted_words:
        result += f"{key} - {value}\n"
    return result

# print(
#     words_sorting(
#         'escape',
#         'charm',
#         'mythology'
#   ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))
# print(
#     words_sorting(
#         'cacophony',
#         'accolade'
#   ))
