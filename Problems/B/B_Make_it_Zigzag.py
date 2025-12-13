from itertools import accumulate

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    prefix_max = list(accumulate(a, max))
    
    INF = 10**18

    count = 0
    for i in range(0,n,2):
        left = prefix_max[i-1] if i-1>=0 else INF
        right = prefix_max[i+1] if i + 1 <= n-1 else INF
        limit = min(left, right)-1
        if a[i] > limit:
            count += (a[i] - limit)
        
    print(count)
    