def shopping_cart(*args):
    result = ""
    products = {
        "Soup": [],
        "Pizza": [],
        "Dessert": []
    }
    limit = 0
    for elem in args:
        if elem == "Stop":
            break
        if elem[0] == "Soup":
            limit = 3
        elif elem[0] == "Pizza":
            limit = 4
        elif elem[0] == "Dessert":
            limit = 2
        products[elem[0]].append(elem[1]) if len(products[elem[0]]) < limit and elem[1] not in products[elem[0]] else None
    sorted_products = sorted(products.items(), key=lambda x: (-len(x[1]), x[0]))
    for items in products.values():
        if len(items) > 0:
            break
    else:
        return "No products in the cart!"
    for products, items in sorted_products:
        result += f"{products}:\n"
        for item in sorted(items):
            result += f" - {item}\n"
    return result



print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
