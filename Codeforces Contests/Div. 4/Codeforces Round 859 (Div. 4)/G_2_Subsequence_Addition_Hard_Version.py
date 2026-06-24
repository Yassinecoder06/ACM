t = int(input())

for _ in range(t):
    n = int(input())

    c = list(map(int, input().split()))
    c.sort()

    if c[0] != 1:
        print('NO')
        continue

    maximus = 1
    i = 1
    ok = True
    while i <= n-1:
        if c[i] > maximus:
            ok = False
            break
        maximus += c[i]
        i+=1

    print('YES') if ok else print('NO')