t = int(input())
for _ in range(t):
    s, k, m = map(int, input().split())

    n = m // k
    r = m % k

    if s >= k:
        # After each flip, the remaining upper sand alternates between s and k.
        x = s if n % 2 == 0 else k
    else:
        # Sand always finishes before the next flip; upper resets to s each time.
        x = s

    if r == 0:
        print(x)
    else:
        remaining = x - r
        print(remaining if remaining > 0 else 0)

