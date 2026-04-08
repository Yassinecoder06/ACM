from math import gcd

n = int(input())
a = int(input())
b = int(input())

if a > b:
    a, b = b, a

can_spend = False
max_x = n // a
for x in range(max_x + 1):
    remaining = n - a * x
    if remaining % b == 0:
        can_spend = True
        break

print("YES" if can_spend else "NO")