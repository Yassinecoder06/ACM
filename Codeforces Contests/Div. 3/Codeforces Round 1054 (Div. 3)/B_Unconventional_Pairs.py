t = int(input())

for _ in range(t):
    n = int(input())

    a = list(map(int, input().split()))
    a.sort()
    m = 0
    for i in range(0,n, 2):
        m = max(m, a[i+1] - a[i])

    print(m)