def solve(n, k):
    for t in range(0,32):
        p = 2**t
        low = n//p
        high = (n+p-1)//p
        if low==k or high==k:
            return t
    return -1

t = int(input())
for _ in range(t):
    c = []
    n,k = map(int, input().split())

    print(solve(n,k))

