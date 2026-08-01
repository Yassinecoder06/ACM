t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    prefix = 0
    ok = True

    for i in range(n):
        prefix += a[i]
        needed = (i + 1) * (i + 2) // 2
        if prefix < needed:
            ok = False
            break

    print('YES' if ok else 'NO')
    

    