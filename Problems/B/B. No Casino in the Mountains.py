t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    hikes = 0
    j = 0
    count = sum(a[:k])
    
    while j + k <= n:
        if count == k:
            hikes += 1
            j += k + 1
            if j + k <= n:
                count = sum(a[j:j+k])
        else:
            if j + k < n:
                count = count - a[j] + a[j+k]
            j += 1

    print(hikes)
