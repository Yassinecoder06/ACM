t = int(input())

output = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    
    count = [0] * (n + 1)
    for i in range(n):
        if a[i] <= n:
            count[a[i]] += 1
    
    caught = [0] * (n + 1)
    
    for v in range(1, n + 1):
        if count[v] == 0:
            continue
        for multiple in range(v, n + 1, v):
            caught[multiple] += count[v]
    
    output.append(str(max(caught)))
print(('\n'.join(output) + '\n'))




    
