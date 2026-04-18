import sys
input = sys.stdin.readline

def tri(x):
    return x * (x + 1) // 2

t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())

    left_limit = k - 1
    right_limit = n - k

    ans = 1

    for L in range(left_limit+1):
        costL = tri(L)
        if costL > m:
            break

        remaining = m - costL

        lo, hi = 0, right_limit
        bestR = 0

        while lo <= hi:
            mid = (lo + hi) // 2
            if tri(mid) <= remaining:
                bestR = mid
                lo = mid + 1
            else:
                hi = mid - 1

        ans = max(ans, 1 + L + bestR)

    print(ans)