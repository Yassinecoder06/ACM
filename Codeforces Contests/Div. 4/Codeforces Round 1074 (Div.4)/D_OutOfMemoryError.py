t = int(input())
for _ in range(t):
    n,m,h = map(int, input().split())
    a = list(map(int, input().split()))

    cur_val = [0]*n
    cur_ver = [0]*n
    ver = 1


    for _ in range(m):
        b,c = map(int, input().split())
        b-=1

        base = cur_val[b] if cur_ver[b] == ver else a[b]
        newv = base + c

        if newv > h:
            ver += 1
        else:
            cur_val[b] = newv
            cur_ver[b] = ver

    for i in range(n):
        cur_val[i] = cur_val[i] if cur_ver[i] == ver else a[i]

    print(*cur_val)