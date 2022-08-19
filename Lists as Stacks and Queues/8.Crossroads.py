from collections import deque

green_lite_duration = int(input())
window_duration = int(input())
command = input()
green_lite_time = 0
cars = deque()
total_cars_passed = 0
while not command == "END":
    if command == "green":
        green_lite_time = green_lite_duration
        while green_lite_time > 0:
            if not cars:
                break
            current_car = cars.popleft()
            if len(current_car) <= green_lite_time:
                green_lite_time -= len(current_car)
                total_cars_passed += 1
            else:
                if len(current_car) <= green_lite_time + window_duration:
                    total_cars_passed += 1
                    window_duration -= len(current_car) - green_lite_time
                    green_lite_time = 0

                else:
                    index = green_lite_time + window_duration
                    print("A crash happened!")
                    print(f"{current_car} was hit at {current_car[index]}.")
                    exit()
    else:
        cars.append(command)

    command = input()

print("Everyone is safe.")
print(f"{total_cars_passed} total cars passed the crossroads.")
