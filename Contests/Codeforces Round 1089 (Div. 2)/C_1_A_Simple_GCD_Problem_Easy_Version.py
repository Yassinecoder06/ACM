from math import gcd

t = int(input())
out = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a = list(map(int, input().split()))

    g = [gcd(a[i], a[i + 1]) for i in range(n - 1)]

    c = [0] * n
    c[0] = g[0]
    c[-1] = g[-1]
    for i in range(1, n - 1):
        c[i] = g[i - 1] * g[i] // gcd(g[i - 1], g[i])

    ans = 0
    for i in range(n):
        if c[i] < a[i]:
            ans += 1

    print(ans)


        
