text = input()
data = {}
for elm in text:
    if elm not in data:
        data[elm] = 0
    data[elm] += 1


for key, value in sorted(data.items()):
    print(f'{key}: {value} time/s')
