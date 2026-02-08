def mex(arr):
    s = set(arr)
    m = 0
    while m in s:
        m += 1
    return m

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    best_mex= mex(a)
    a.sort()
    for i in range(n):
        x = -a[i]
        b = [a[j] + x for j in range(n)]

        best_mex = max(best_mex, mex(b))

    print(best_mex)

