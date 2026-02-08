t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    total_cost = 0
    for i in range(n - 1):
        total_cost += abs(a[i] - a[i + 1])
    
    max_savings = 0

    for k in range(n):
        if k == 0:
            savings = abs(a[0] - a[1])
        elif k == n - 1:
            savings = abs(a[n - 2] - a[n - 1])
        else:
            lost = abs(a[k - 1] - a[k]) + abs(a[k] - a[k + 1])
            gained = abs(a[k - 1] - a[k + 1])
            savings = lost - gained
        
        max_savings = max(max_savings, savings)
    
    min_time = total_cost - max_savings
    print(min_time)