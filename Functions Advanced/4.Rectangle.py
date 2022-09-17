def rectangle(length, width):
    try:
        def area(length, width):
            return length * width

        def perimeter(length, width):
            return 2 * length + 2 * width

        area_ = area(length, width)
        perim = perimeter(length, width)
        return f"Rectangle area: {area_}\nRectangle perimeter: {perim}"
    except:
        return "Enter valid values!"


print(rectangle(2, 10))
