import math

t = int(input())

for _ in range(t):
    n, x = map(int, input().split())

    a, b, c = [], [], []

    for _ in range(n):
        ai, bi, ci = map(int, input().split())
        a.append(ai)
        b.append(bi)
        c.append(ci)

    m = max(a[i] * b[i] - c[i] for i in range(n))
    s = sum(a[i] * (b[i] - 1) for i in range(n))

    x -= s

    if (x<= 0):
        print(0)
        continue
    
    if (m <= 0):
        print(-1)
        continue

    print((x + m - 1) // m)