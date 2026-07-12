t = int(input())
for _ in range(t):
    n,_ = map(int,input().split())
    a = list(map(int,input().split()))
    b = int(input())
    
    new = []
    for i in range(n):
        new.append(b - a[i])

    m = - float('inf')
    ok = True
    
    for i in range(n):
        if min(a[i], new[i]) >= m:
            m = min(a[i], new[i])
        elif new[i] >= m:
            m = new[i]
        elif a[i] >= m:
            m = a[i]
        else:
            ok = False
            break

    print('YES') if ok else print('NO')
