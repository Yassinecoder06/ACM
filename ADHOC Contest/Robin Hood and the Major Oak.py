t = int(input())
results = []
for _ in range(t):
    n, k = map(int, input().split())
    
    sum_n = n * (n + 1) // 2
    sum_n_k = (n - k) * (n - k + 1) // 2 if k < n else 0
    total_leaves = sum_n - sum_n_k

    if total_leaves % 2 == 0:
        results.append('yes')
    else: 
        results.append('no')

for result in results:
    print(result)
    