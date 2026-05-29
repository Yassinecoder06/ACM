t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    maximum = n

    x1 = p.index(maximum)
    x2 = p[0]

    p[0] = p[x1] 
    p[x1] = x2

    print(" ".join(map(str, p)))
