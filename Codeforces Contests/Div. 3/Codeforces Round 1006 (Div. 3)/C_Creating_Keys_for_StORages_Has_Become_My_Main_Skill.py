t = int(input())
output = []
for _ in range(t):
    n,x = map(int, input().split())
    
    res = []
    curr = 0
    while len(res) < n and curr < n:
        if (curr | x) == x:
            res.append(curr)
        curr += 1
    
    while len(res) < n:
        res.append(0)
        
    current_or = 0
    for val in res:
        current_or |= val
        
    if current_or != x:
        res[-1] = x
        
    output.append(" ".join(map(str, res)))

print("\n".join(output))