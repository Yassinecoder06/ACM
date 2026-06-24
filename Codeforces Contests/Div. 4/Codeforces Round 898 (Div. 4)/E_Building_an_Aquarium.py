import bisect

t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()

    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + a[i - 1]

    low = 1
    high = 2 * 10**9 + 7
    ans = 0

    while low <= high:
        mid = (low + high) // 2

        idx = bisect.bisect_right(a, mid)

        needed = mid * idx - prefix_sum[idx]

        if needed <= x:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    print(ans)