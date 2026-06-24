t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    down = False
    up = False
    valley = False
    ok = True
    for i in range(1,n):
        if a[i-1] < a[i] and not up:
            up = True

        if a[i-1] > a[i] and not down:
            down = True
                 
        if a[i-1] < a[i] and down and not valley:
            down = False
            up = True
            valley = True
        
        if a[i-1] > a[i] and up and valley:
            ok = False
            break


        if a[i-1] > a[i] and up:
            ok = False
            break


    print('YES') if ok else print('NO')