t = int(input())

for _ in range(t):
    n = int(input())

    a = list(map(int, input().split()))

    mx = 0
    ans = 0
    for i in range(n):
        if a[i] >= mx:
            mx = a[i]
            ans += 1

    print(ans)