from collections import Counter
from math import factorial
t = int(input())

for _ in range(t):
    n = int(input())
    
    a = []
    c = Counter()
    for _ in range(n):
        a.append(list(map(int, input().split())))
        c.update(Counter(a[-1]))

    ok = True
    for key in c.keys():
        if c[key] > n**2 - n:
            ok = False
            break

    if ok: print("YES")
    else:
        print("NO")