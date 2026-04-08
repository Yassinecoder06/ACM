t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    a = list(map(int, input().split()))
    k-=1
    s1 = 0
    s2 = 0
    path1 = True
    path2 = True
    for i in range(k, -1, -1):
        s1 += a[i]
        if s1 < 0:
            path1 = False
    
    for i in range(k, n):
        s2 += a[i]
        if s2 < 0:
            path2 = False
            
    
    if path1 or path2:
        print("YES")
    else:
        print("NO")
        
    
    