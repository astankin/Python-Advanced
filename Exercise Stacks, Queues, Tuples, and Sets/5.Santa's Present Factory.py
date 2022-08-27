from collections import deque

materials = [int(num) for num in input().split()]
magic_level = deque(int(num) for num in input().split())

crafting_table = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}
toys = {}

while materials and magic_level:
    material = materials.pop()
    magic = magic_level.popleft()
    if material == 0 and magic == 0:
        continue
    if material == 0:
        magic_level.appendleft(magic)
        continue
    if magic == 0:
        materials.append(material)
        continue
    result = material * magic
    if result in crafting_table:
        toy = crafting_table[result]
        if toy not in toys:
            toys[toy] = 0
        toys[toy] += 1
    else:
        if result < 0:
            materials.append(material + magic)
        elif result > 0 :
            materials.append(material + 15)
if ("Doll" in toys and "Wooden train" in toys) or ("Teddy bear" in toys and "Bicycle" in toys):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join(str(num) for num in reversed(materials))}")
if magic_level:
    print(f"Magic left: {', '.join(str(num) for num in magic_level)}")
for toy, count in sorted(toys.items()):
    print(f"{toy}: {count}")