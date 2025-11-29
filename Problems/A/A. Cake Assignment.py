t = int(input())
for _ in range(t):
    k,x = map(int, input().split())
    T = 2**(k+1)
    S = 2**k
    cur = x
    rev_ops = []
    i = 0
    while cur!=S:
        if cur < S:
            cur = cur * 2
            rev_ops.append("1")
            i += 1
        else:
            cur = cur*2 - T
            rev_ops.append("2")
            i += 1
    
    rev_ops = rev_ops[::-1]
    print(i)
    print(" ".join(rev_ops))

            