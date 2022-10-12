def print_top_part(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(j + 1, end=" ")
        print()


def print_bottom_part(n):
    for i in range(n, 0, -1):
        for j in range(1, i):
            print(j, end=" ")
        print()


def print_triangle(n):
    print_top_part(n)
    print_bottom_part(n)

