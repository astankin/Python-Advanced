def vip_check(code):
    return code[0].isdigit()


vip_list = set()
regular_guests = set()
n = int(input())
for _ in range(n):
    reservation_code = input()
    if vip_check(reservation_code):
        vip_list.add(reservation_code)
    else:
        regular_guests.add(reservation_code)
while True:
    guest_name = input()
    if guest_name == "END":
        break
    if vip_check(guest_name):
        vip_list.remove(guest_name)
    else:
        regular_guests.remove(guest_name)

print(len(vip_list) + len(regular_guests))
[print(code) for code in sorted(vip_list)]
[print(code) for code in sorted(regular_guests)]
