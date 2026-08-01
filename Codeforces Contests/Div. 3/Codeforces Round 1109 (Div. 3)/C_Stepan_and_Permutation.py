from math import gcd

t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    p = list(map(int, input().split()))

    g = gcd(x, y)
    ok = True

    for i, value in enumerate(p, start=1):
        if (i - value) % g != 0:
            ok = False
            break

    print('YES' if ok else 'NO')
