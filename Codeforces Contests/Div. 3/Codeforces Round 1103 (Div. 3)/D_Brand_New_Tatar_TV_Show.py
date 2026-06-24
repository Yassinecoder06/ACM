t = int(input())
out = []
for _ in range(t):
    n,k = map(int, input().split())

    a = list(map(int, input().split())) 
    a.sort()
    
    possible = False
    current_comp_size = 1
    
    for i in range(1, n):
        if a[i] - a[i-1] <= k:
            current_comp_size += 1
        else:
            if current_comp_size % 2 != 0:
                possible = True
            current_comp_size = 1  
    
    if current_comp_size % 2 != 0:
        possible = True
        
    if possible:
        out.append("YES")
    else:
        out.append("NO")
        
print('\n'.join(out))