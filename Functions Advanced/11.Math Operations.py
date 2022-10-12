def math_operations(*args, **kwargs):
    result = []
    keys = {
        0: "a",
        1: "s",
        2: "d",
        3: "m",
    }
    for i in range(len(args)):
        if i % 4 == 0:
            kwargs[keys[i % 4]] += args[i]
        elif i % 4 == 1:
            kwargs[keys[i % 4]] -= args[i]
        elif i % 4 == 2 and args[i] != 0:
            kwargs[keys[i % 4]] /= args[i]
        elif i % 4 == 3:
            kwargs[keys[i % 4]] *= args[i]
    sorted_kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    for key, value in sorted_kwargs:
        result.append(f"{key}: {value:.1f}")
    return '\n'.join(result)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))

print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))

print(math_operations(6.0, a=0, s=0, d=5, m=0))
