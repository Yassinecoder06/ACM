t = int(input())

for _ in range(t):
    n = int(input())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b = b[1:] + [0]

    m = 0
    s = 0

    for i in range(n):
        if a[i] > b[i]:
            m += a[i]
            s += b[i]

    print(m-s)