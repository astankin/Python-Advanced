from collections import deque

elfs = deque(map(int, input().split()))
materials = list(map(int, input().split()))
total_toys = 0
energy = 0
counter = 0
while elfs and materials:
    target_toys = 1
    spent_energy = 0
    counter += 1
    created_toys = 0
    additional_energy = 1
    elf_energy = elfs.popleft()
    if elf_energy < 5:
        continue
    box = materials.pop()
    needed_energy = box
    if counter % 3 == 0:
        needed_energy = box * 2
        target_toys = 2
    if counter % 5 == 0:
        created_toys = 0
        additional_energy = 0
    if elf_energy >= needed_energy:
        created_toys = target_toys
        elf_energy -= needed_energy
        energy += needed_energy
    else:
        materials.append(box)
        additional_energy = elf_energy

    elfs.append(elf_energy + additional_energy)
    total_toys += created_toys


print(f"Toys: {total_toys}")
print(f"Energy: {energy}")
if elfs:
    print(f"Elves left: {', '.join(map(str, elfs))}")
if materials:
    print(f"Boxes left: {', '.join(map(str, materials))}")