def even_odd_filter(**kwargs):
    new_dict = {}
    for command, value in kwargs.items():
        parity = 0 if command == "even" else 1
        new_dict[command] = [x for x in value if x % 2 == parity]
    return dict(sorted(new_dict.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
