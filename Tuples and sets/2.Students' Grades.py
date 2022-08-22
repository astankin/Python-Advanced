def average(students):
    return sum(students) / len(students)


n = int(input())
students_info = {}
while n > 0:
    name, grade = input().split()
    grade = float(grade)
    if name not in students_info:
        students_info[name] = []
    students_info[name].append(grade)
    n -= 1


for name, info in students_info.items():
    average_grade = average(students_info[name])
    print(f"{name} -> {' '.join(f'{grade:.2f}' for grade in info)} (avg: {average_grade:.2f})")
