from math import gcd
from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ind = defaultdict(int)

    max_index = {}
    for i in range(n):
        max_index[a[i]] = i + 1 
    
    result = -1
    
    for v1, i1 in max_index.items():
        for v2, i2 in max_index.items():
            if gcd(v1, v2) == 1:
                result = max(result, i1 + i2)
    print(result)

