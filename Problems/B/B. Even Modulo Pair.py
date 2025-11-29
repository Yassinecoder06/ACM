t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ok = False
    for i in range(n-1):
        x = a[i]
        for j in range(i+1,n):
            y = a[j]
            if (y % x)%2 == 0:
                print(x, y)
                ok = True
                break
        if ok: break
    if not ok: print(-1)
