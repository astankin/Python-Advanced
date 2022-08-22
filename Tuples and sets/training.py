from collections import OrderedDict

my_dict = {'a': 10, 'b': 0, 'c': 3, 'd': 1, 'e': 5 }

sort_orders = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=False))
print(sort_orders)
dict1 = OrderedDict(sorted(my_dict.items()))
print(dict1)

dictionary_keys = list(my_dict.keys())
