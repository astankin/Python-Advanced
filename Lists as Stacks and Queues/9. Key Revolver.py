from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(num) for num in input().split()]
locks = deque(int(num) for num in input().split())
intelligence = int(input())
counter = 0
total_bullets_shot = 0
while len(bullets) > 0 and len(locks) > 0:
    bullet = bullets.pop()
    lock = locks.popleft()
    if bullet <= lock:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(lock)
    counter += 1
    total_bullets_shot += 1
    if counter == gun_barrel_size and bullets:
        print("Reloading!")
        counter = 0
money_earned = intelligence - (total_bullets_shot * bullet_price)
if not bullets and locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
if not locks:
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")