t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    l = 0
    r = n - 1

    s1 = 0
    s2 = 0
    ans = 0

    while l <= r:
        if s1 <= s2:
            s1 += a[l]
            l += 1
        else:
            s2 += a[r]
            r -= 1

        if s1 == s2:
            ans = l + (n - 1 - r)

    print(ans)
