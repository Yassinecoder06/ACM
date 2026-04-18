t = int(input())

for _ in range(t):
    n = int(input())
    c = []
    p = []
    for i in range(n):
        c1, p1 = map(int, input().split())
        c.append(c1)
        p.append(p1/100.0)

    ans = 0
    for i in range(n-1, -1, -1):
        ans = max(ans, ans*(1-p[i])+c[i])

    print(ans)



