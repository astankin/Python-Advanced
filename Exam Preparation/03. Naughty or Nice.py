def naughty_or_nice_list(*args, **kwargs):
    def only_one_tuple_check(santa_list, el_check):
        tuple_ = tuple()
        counter = 0
        for elem in santa_list:
            if el_check in elem:
                tuple_ = elem
                counter += 1
        if counter == 1:
            return tuple_
        return False

    def removing_elem(condition):
        elem_to_be_removed = condition
        name = elem_to_be_removed[1]
        new_santa_list[behavior].append(name)
        santa_list.remove(elem_to_be_removed)

    santa_list = args[0]
    commands = args[1:]
    new_santa_list = {"Nice": [], "Naughty": [], "Not found": []}
    for command in commands:
        number = int(command.split("-")[0])
        behavior = command.split("-")[1]
        condition = only_one_tuple_check(santa_list, number)
        if condition:
            removing_elem(condition)
    if kwargs:
        for name, behavior in kwargs.items():
            condition = only_one_tuple_check(santa_list, name)
            if condition:
                removing_elem(condition)
    for elem in santa_list:
        name = elem[1]
        new_santa_list["Not found"].append(name)
    result = ""
    for behavior, names in new_santa_list.items():
        if names:
            result += f"{behavior}: {', '.join(names)}\n"
    return result


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
))

print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
