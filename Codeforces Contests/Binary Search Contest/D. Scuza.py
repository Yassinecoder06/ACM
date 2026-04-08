t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = list(map(int, input().split()))
    

    prefix_sum = [0] * (n + 1)
    prefix_max = [0] * n
    
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + a[i]
        if i == 0:
            prefix_max[i] = a[i]
        else:
            prefix_max[i] = max(prefix_max[i - 1], a[i])
    
    results = []
    for query in k:
        left, right = 0, n - 1
        idx = -1
        
        while left <= right:
            mid = (left + right) // 2
            if prefix_max[mid] <= query:
                idx = mid
                left = mid + 1
            else:
                right = mid - 1
        
        if idx == -1:
            results.append(0)
        else:
            results.append(prefix_sum[idx + 1])
    
    print(" ".join(map(str, results)))