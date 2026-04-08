import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
m = int(input())

devices = []
for _ in range(m):
    val, typ = input().split()
    devices.append((int(val), typ))

devices.sort(key=lambda x: x[0])

equipped = total_cost = 0
for price, typ in devices:
    if typ == "USB" and a > 0:
        a -= 1
    elif typ == "PS/2" and b > 0:
        b -= 1
    elif c > 0:
        c -= 1
    else:
        continue
    equipped += 1
    total_cost += price

print(equipped, total_cost)
