t = int(input())

for _ in range(t):
    n,c,k = map(int, input().split())

    a = list(map(int, input().split()))
    a.sort()

    for i in range(n):
        if c >= a[i]:
            use = min(k, c - a[i])
            a[i] += use
            k -= use
            
            c += a[i]
        else:
            pass
        
    print(c)
    
