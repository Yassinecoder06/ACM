t = int(input())
for _ in range(t):
    n,m,x,y = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        if a[i] <= y:
            ans += 1
        else:
            break

    for j in range(m):
        if b[j] <= x:
            ans += 1
        else:
            break

    print(ans)

        