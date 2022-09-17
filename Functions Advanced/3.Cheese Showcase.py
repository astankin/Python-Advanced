def sorting_cheeses(**kwargs):
    result = ""
    sorted_cheeses = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    for cheese, quantity in sorted_cheeses:
        quantity = sorted(quantity, reverse=True)
        result += cheese + "\n"
        result += '\n'.join(str(x) for x in quantity) + "\n"
    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125]
    )
)
