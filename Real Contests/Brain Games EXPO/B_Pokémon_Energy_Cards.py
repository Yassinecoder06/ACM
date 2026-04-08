from math import gcd

x, y = map(int, input().split())

g = gcd(x, y)
is_power_of_two = (g & (g - 1)) == 0

print("YES" if is_power_of_two else "NO")
