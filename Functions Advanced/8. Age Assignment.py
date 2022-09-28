import os


def age_assignment(*args, **kwargs):
    result = {}
    output = []
    for letter, age in kwargs.items():
        for name in args:
            if name.startswith(letter):
                result[name] = age
    sorted_result = sorted(result.items(), key=lambda x: x[0])
    for name, age in sorted_result:
        output.append(f"{name} is {age} years old.")
    return os.linesep.join(output)




print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
