t = int(input())

for _ in range(t):
    n = int(input())
    mx = 0
    results = {}
    for x in range(2,n+1):
        k = n//x
        results[x] = x * (k*(k+1)//2)
    
    results = sorted(results.items(), key=lambda x:x[1], reverse=True)
    print(results[0][0])