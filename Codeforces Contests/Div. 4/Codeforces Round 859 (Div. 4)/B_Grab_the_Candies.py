t = int(input())

for _ in range(t):
    n = int(input())

    a = list(map(int, input().split()))

    m = 0
    b = 0
    for i in range(n):
        if a[i]%2==0:
            m += a[i]
        else:
            b += a[i]

    print('YES') if m > b else print('NO')