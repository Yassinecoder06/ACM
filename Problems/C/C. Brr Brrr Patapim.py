t = int(input())
for _ in range(t):
    n = int(input())
    p = [0]*(2*n)
    s = (2*n)*((2*n)+1) // 2
    k = n + 1
    for i in range(n):
        a = list(map(int, input().split()))
        if i == 0:
            for j in range(n):
                p[j+1] = a[j]
                s -= a[j]
        else:
            p[k] = a[-1]
            s -= a[-1]
            k += 1
    p[0] = s
    for i in range(2*n):
        p[i] = str(p[i])
    print(" ".join(p))
    