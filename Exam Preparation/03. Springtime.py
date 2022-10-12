import os


def start_spring(**kwargs):
    objects = {}
    result = []
    for key, value in kwargs.items():
        if value not in objects:
            objects[value] = []
        objects[value].append(key)
    sorted_objects = sorted(objects.items(), key=lambda x: (-len(x[1]), x[0]))
    for key, value in sorted_objects:
        result.append(f"{key}:")
        for elem in sorted(value):
            result.append(f"-{elem}")
    return os.linesep.join(result)




example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))


