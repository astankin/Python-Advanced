def list_manipulator(list_, *args):
    command = args[0]
    new_list = []
    if command == "add":
        if args[1] == "beginning":
            new_list = list(args[2:]) + list_
        elif args[1] == "end":
            new_list = list_ + list(args[2:])
    elif command == "remove":
        if args[1] == "beginning":
            if len(args) > 2:
                new_list = list_[args[2]:]
            else:
                new_list = list_[1:]
        elif args[1] == "end":
            if len(args) > 2:
                el = len(list_) - args[2]
                new_list = list_[:el]
            else:
                new_list = list_[:-1]
    return new_list


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
