t = int(input())

for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))

    if sum(a) < s:
        print(-1)
        continue

    if s == 0:
        ans = 0
        cur = 0
        for x in a:
            if x == 0:
                cur += 1
                ans = max(ans, cur)
            else:
                cur = 0
        print(n - ans)
        continue

    l = 0
    cur = 0
    best = 0

    for r in range(n):
        cur += a[r]

        while cur > s:
            cur -= a[l]
            l += 1

        if cur == s:
            best = max(best, r - l + 1)

    print(n - best)