import os


def shopping_list(budget, **kwargs):
    bought_items = []
    result = []
    bought_items_count = 0
    if budget < 100:
        return "You do not have enough budget."
    for item, value in kwargs.items():
        price = float(value[0])
        count = int(value[1])
        amount = count * price
        if budget >= amount:
            bought_items.append(item)
            budget -= amount
            bought_items_count += 1
            result.append(f"You bought {item} for {amount:.2f} leva.")
            if bought_items_count == 5:
                break
    return os.linesep.join(result)





print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
