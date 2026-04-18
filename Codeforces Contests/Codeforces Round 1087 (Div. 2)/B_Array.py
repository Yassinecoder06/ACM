t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    out = []
    
    for i in range(n):
        greater = 0  
        less = 0     
        
        for j in range(i + 1, n):
            if a[j] > a[i]:
                greater += 1
            elif a[j] < a[i]:
                less += 1
        
        
        out.append(str(max(greater, less)))
    
    print(" ".join(out))