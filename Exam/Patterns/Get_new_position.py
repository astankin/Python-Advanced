def moving(direction, row, col):
    if direction == "up":
        row -= 1
    elif direction == "down":
        row += 1
    elif direction == "left":
        col -= 1
    elif direction == "right":
        col += 1
    return row, col


def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_new_position(row, col, size):
    if row >= size:
        row = 0
    if row < 0:
        row = size - 1
    if col >= size:
        col = 0
    if col < 0:
        col = size - 1
    return row, col

#-----------------------------------------------


def get_new_position(direction, row, col, size):

    def moving_to_the_opposite_side(r, c, s):
        if r >= s:
            r = 0
        if r < 0:
            r = s - 1
        if c >= s:
            c = 0
        if c < 0:
            c = s - 1
        return r, c
    if direction == "up":
        row -= 1
    elif direction == "down":
        row += 1
    elif direction == "left":
        col -= 1
    elif direction == "right":
        col += 1
    if 0 <= row < size and 0 <= col < size:
        return row, col
    else:
        return moving_to_the_opposite_side(row, col, size)


#-----------------------------------------------------------------------

def get_new_position(direction, row, col, size):

    def is_inside(row_, col_):
        return 0 <= row_ < size and 0 <= col_ < size

    def moving_to_the_opposite_side(r, c, s):
        if r >= s:
            r = 0
        if r < 0:
            r = s - 1
        if c >= s:
            c = 0
        if c < 0:
            c = s - 1
        return r, c

    new_coordinates = {
        "up": (row - 1, col),
        "down": (row + 1, col),
        "left": (row, col - 1),
        "right": (row, col + 1)
    }
    row, col = new_coordinates[direction]
    if is_inside(row, col):
        return row, col
    else:
        return moving_to_the_opposite_side(row, col, size)

