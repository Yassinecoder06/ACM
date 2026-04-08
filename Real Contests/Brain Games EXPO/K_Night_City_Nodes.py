from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    
    c = Counter(r)
    print(c[3] + c[1])