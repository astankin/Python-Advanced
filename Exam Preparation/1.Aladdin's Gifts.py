from collections import deque

gifts = {
    (100, 199): "Gemstone",
    (200, 299): "Porcelain Sculpture",
    (300, 399): "Gold",
    (400, 499): "Diamond Jewellery"
}
created_gifts = {"Gemstone": 0, "Porcelain Sculpture": 0, "Gold": 0, "Diamond Jewellery": 0}
materials = list(map(int, input().split()))
magic_levels = deque(map(int, input().split()))

while materials and magic_levels:
    current_material = materials.pop()
    magic = magic_levels.popleft()
    result = current_material + magic
    if result < 100:
        if result % 2 == 0:
            result = current_material * 2 + magic * 3
        else:
            result *= 2
    elif result > 499:
        result = result / 2
    for range_, gift in gifts.items():
        if range_[0] <= result <= range_[1]:
            created_gifts[gift] += 1
            break

if (created_gifts["Gemstone"] != 0 and created_gifts["Porcelain Sculpture"] != 0) \
        or (created_gifts["Gold"] != 0 and created_gifts["Diamond Jewellery"] != 0):

    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")


if materials:
    print(f"Materials left: {', '.join(map(str, materials))}")
if magic_levels:
    print(f"Magic left: {', '.join(map(str, magic_levels))}")

sorted_created_gifts = sorted(created_gifts.items(), key=lambda x: x[0])
for item, count in sorted_created_gifts:
    if count != 0:
        print(f"{item}: {count}")
