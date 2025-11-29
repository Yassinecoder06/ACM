t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    
    prefix = [0] * (n+1)
    for i in range(n):
        prefix[i+1] = prefix[i] + a[i]
    
    max_sum = 0
    for x in range(k+1):
        left = 2*x
        right = n - (k - x)
        if left <= right:
            current_sum = prefix[right] - prefix[left]
            max_sum = max(max_sum, current_sum)
    
    print(max_sum)
