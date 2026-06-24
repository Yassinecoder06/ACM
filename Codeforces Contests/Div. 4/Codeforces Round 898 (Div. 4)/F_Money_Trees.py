t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    a = list(map(int, input().split()))
    h = list(map(int, input().split()))

    left = 0
    cur = 0
    ans = 0

    for right in range(n):
        if right > 0 and h[right - 1] % h[right] != 0:
            left = right
            cur = 0

        cur += a[right]

        while cur > k:
            cur -= a[left]
            left += 1

        ans = max(ans, right - left + 1)

    print(ans)

