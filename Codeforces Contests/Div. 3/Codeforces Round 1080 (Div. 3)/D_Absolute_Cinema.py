t = int(input())
for _ in range(t):
    n = int(input())
    f = list(map(int, input().split()))
    if n == 2:
        a = [f[1], f[0]]
    else:
        a = [0] * n
        for i in range(1, n - 1):
            a[i] = (f[i + 1] - 2 * f[i] + f[i - 1]) // 2
        S = sum(a[1:n - 1])
        T = sum((i + 1) * a[i] for i in range(1, n - 1))
        a[n - 1] = (f[0] - T + S) // (n - 1)
        a[0] = a[n - 1] + f[1] - f[0] + S
    print(' '.join(map(str, a)))
