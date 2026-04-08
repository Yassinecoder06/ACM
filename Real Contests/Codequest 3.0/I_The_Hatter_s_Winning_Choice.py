import sys

def vcount(n, p):
    c = 0
    while n % p == 0:
        n //= p
        c += 1
    return c

def solve():
    t = int(input())
    res = []
    for _ in range(t):
        x = int(input())
        k = len(str(x))
        a = min(vcount(x, 2), k)
        b = min(vcount(x, 5), k)
        res.append(str((a+1)*(b+1)))
    print("\n".join(res))


solve()
