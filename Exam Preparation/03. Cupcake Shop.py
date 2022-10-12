def stock_availability(inventory_list, command, *args):
    if command == "delivery":
        for box in args:
            inventory_list.append(box)
    elif command == "sell":
        if args:
            for el in args:
                if isinstance(el, int):
                    inventory_list = inventory_list[int(el):]
                else:
                    for elem in args:
                        if elem in inventory_list:
                            inventory_list = [x for x in inventory_list if x != elem]
        else:
            inventory_list.remove(inventory_list[0])

    return inventory_list






# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
