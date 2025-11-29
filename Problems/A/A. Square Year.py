from math import sqrt

t = int(input())
for _ in range(t):
    s = input().strip(" ")
    if sqrt(int(s)).is_integer():
        a = int(sqrt(int(s)) // 2)
        b = int(sqrt(int(s)) - a)
        print(f"{a} {b}")
    else:
        print(-1)

#Accepted
