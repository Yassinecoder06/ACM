t = int(input())

for _ in range(t):
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))

    sall = sum(v // x for v in a)

    ans = 0
    for v in a:
        si = sall - (v // x)
        ans = max(ans, v + si * y)

    print(ans)
