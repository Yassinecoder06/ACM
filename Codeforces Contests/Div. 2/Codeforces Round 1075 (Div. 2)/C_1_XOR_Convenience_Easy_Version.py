t = int(input())

def mex(arr):
    arr = set(arr)
    t = 0
    while t in arr:
        t+=1
    return t

for _ in range(t):
    n = int(input())
    p = [1]*n

    for i in range(n-2, -1, -1):
        p[i] = p[n-1] ^ (i+1)

    p[0] = mex(p)
    p = list(map(str, p))

    print(" ".join(p))