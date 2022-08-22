import time
import numpy as np
arr = np.array([])
list_1 = []
count = 2 ** 15
result = 0
start = time.time()
for i in range(count):
    list_1.append(i)
while list_1:
    result += list_1.pop()
end = time.time()
print(end - start)
start = time.time()
for i in range(count):
    list_1.insert(0, i)
while list_1:
    result += list_1.pop(0)
end = time.time()
print(end-start)

