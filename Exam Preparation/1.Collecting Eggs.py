from collections import deque

eggs = deque(int(x) for x in input().split(", "))
paper = deque(int(x) for x in input().split(", "))
filled_boxes_count = 0

while eggs and paper:
    current_egg = eggs.popleft()
    if current_egg <= 0:
        continue
    if current_egg == 13:
        paper[0], paper[-1] = paper[-1], paper[0]
        continue
    current_paper = paper.pop()
    if current_egg + current_paper <= 50:
        filled_boxes_count += 1

if filled_boxes_count > 0:
    print(f"Great! You filled {filled_boxes_count} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")
if eggs:
    print(f"Eggs left: {', '.join(str(x) for x in eggs)}")
if paper:
    print(f"Pieces of paper left: {', '.join(str(x) for x in paper)}")