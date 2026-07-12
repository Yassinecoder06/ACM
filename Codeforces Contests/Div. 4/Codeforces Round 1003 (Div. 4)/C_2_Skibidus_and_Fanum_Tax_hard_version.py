import bisect

t = int(input())

out = []
for _ in range(t):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    b.sort()

    prev = min(a[0], b[0] - a[0])
        
    possible = True
    
    for i in range(1, n):
        target = a[i] + prev
        idx = bisect.bisect_left(b, target)
        
        val1 = a[i] if a[i] >= prev else float('inf')
        val2 = (b[idx] - a[i]) if idx < m else float('inf')
        
        best = min(val1, val2)
        
        if best == float('inf'):
            possible = False
            break
        else:
            prev = best
            
    out.append("YES" if possible else "NO")
    
print('\n'.join(out))
