t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    h = list(map(int, input().split()))
    ok = True
    time = h[k-1]
    h.sort()
    pos = h.index(time)
    for i in range(pos, n-1):
        if abs(h[i] - h[i+1]) > time:
            ok = False
            break

    if ok:
        print("Yes")
    else:
        print("No")

#Accepted