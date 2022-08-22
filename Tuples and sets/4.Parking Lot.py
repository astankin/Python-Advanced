n = int(input())
cars = set()
for _ in range(n):
    directions, car_number = input().split(", ")
    if directions == "IN":
        cars.add(car_number)
    elif directions == "OUT":
        cars.remove(car_number)
if cars:
    [print(number) for number in cars]
else:
    print("Parking Lot is Empty")
