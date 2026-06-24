t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort(reverse=True)

    ok = True
    for i in range(n-1):
        if a[i] == a[i+1]:
            ok = False
            break
    
    if ok:
        print(" ".join(map(str, a)))
    else:
        print(-1)