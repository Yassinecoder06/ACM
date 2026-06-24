t = int(input())

for _ in range(t):
    n,k = map(int, input().split())

    a = list(map(int, input().split()))
    a.sort()

    max_len = 1
    current_len = 1
    for i in range(1, n):
        if a[i] - a[i-1] <= k:
            current_len += 1
        else:
            max_len = max(max_len, current_len)
            current_len = 1
    
    max_len = max(max_len, current_len)
    print(n - max_len)

    