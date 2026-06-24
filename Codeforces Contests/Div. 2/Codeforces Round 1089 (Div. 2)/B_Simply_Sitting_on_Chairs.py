t = int(input())

for _ in range(t):
    n = int(input())
    p = [x - 1 for x in map(int, input().split())]
    
    pos = [0] * n
    for i, v in enumerate(p):
        pos[v] = i
    
    bad_prefix = [0] * n
    for v in range(n):
        bad_prefix[v] = (bad_prefix[v - 1] if v > 0 else 0) + (1 if pos[v] < v else 0)

    ans = n - bad_prefix[n - 1]    
    print(ans)
