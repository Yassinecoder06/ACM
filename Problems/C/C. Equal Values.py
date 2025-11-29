import sys
from collections import defaultdict

def main():
    t = int(input())
    index = 1
    results = []
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        
        d = defaultdict(list)
        for i in range(n):
            d[a[i]].append(i)
            
        ans = float('inf')
        for x, positions in d.items():
            positions.sort()
            k = len(positions)
            cost = positions[0] * x + (n - positions[-1] - 1) * x
            for j in range(k-1):
                gap = positions[j+1] - positions[j] - 1
                if gap > 0:
                    cost += min(positions[j+1] * x, (n - positions[j] - 1) * x)
            if cost < ans:
                ans = cost
                
        results.append(str(ans))
    
    print("\n".join(results))

main()
