t = int(input())

for _ in range(t):
    n,s,m = map(int, input().split())
    last_r = 0
    ok = False
    for i in range(n):
        l,r = map(int, input().split())
        if l-last_r >= s:
            ok = True

        last_r = r

    if m - last_r>= s:
        ok = True
        

    if ok:
        print('YES')
    else:
        print("NO")

