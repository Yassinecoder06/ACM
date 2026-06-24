from bisect import bisect_left

t = int(input())

for _ in range(t):
    n,q = map(int, input().split())

    a = list(map(int, input().split()))
    a.sort(reverse=True)
    
    prefix_sum = [0] * (n+1)
    for i in range(1,n+1):
        prefix_sum[i] = prefix_sum[i-1] + a[i-1]

    for _ in range(q):
        x = int(input())
        if x > prefix_sum[n]:
            print(-1)
        else:
            print(bisect_left(prefix_sum, x))


        
