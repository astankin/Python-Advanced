from collections import deque


def creating_robots_dict(robots_info):
    robots = {}
    for robot in robots_info:
        name = robot.split("-")[0]
        processing_time = robot.split("-")[1]
        robots[name] = int(processing_time)
    return robots


def starting_time_in_seconds(time):
    time_in_seconds = int(time[0]) * 360 + int(time[1]) * 60 + int(time[2])
    return time_in_seconds


def product_queue():
    products = deque()
    product = input()
    while not product == "End":
        products.append(product)
        product = input()
    return products



robots_info = input().split(";")
robots_dict = creating_robots_dict(robots_info)
time = input().split(":")
starting_time = starting_time_in_seconds(time)
products = product_queue()
processing_robots = {}
available_robots = [k for k in robots_dict.keys()]


def to_str_time(time_in_seconds):
    hours = time_in_seconds // 3600
    minutes = (time_in_seconds % 3600) // 60
    seconds = (time_in_seconds % 3600) % 60
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


while products:
    time_in_seconds = (starting_time + 1) % (24 * 60 * 60)

    for robot_name in [k for k in processing_robots.keys()]:
        processing_robots[robot_name] -= 1
        if processing_robots[robot_name] <= 0:
            processing_robots.pop(robot_name)

    current_product = products.popleft()
    for robot_name in available_robots:
        if robot_name not in processing_robots:
            print(f'{robot_name} - {current_product} [{to_str_time(time_in_seconds)}]')
            processing_robots[robot_name] = robots_dict[robot_name]
            break
    else:
        products.append(current_product)
