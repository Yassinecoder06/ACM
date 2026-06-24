t = int(input())

results = []

for _ in range(t):
    n = int(input())
    ans = []
    
    if n % 2 == 0:
        for i in range(0, n, 2):
            ans.extend([i + 2, i + 1, i + 1, i + 2, i + 1, i + 2, i + 2, i + 1])
    else:
        ans.extend([3, 3, 2, 1, 1, 2, 1, 2, 2, 3, 1, 3])
        for i in range(3, n, 2):
            ans.extend([i + 2, i + 1, i + 1, i + 2, i + 1, i + 2, i + 2, i + 1])
            
    results.append(" ".join(map(str, ans)))
    
print("\n".join(results)) 