


t = int(input())


results = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    count1 = [0] * 30
    for x in a:
        for j in range(30):
            if (x >> j) & 1:
                count1[j] += 1
    
    max_sum = 0
    for x in a:
        current_sum = 0
        for j in range(30):
            if (x >> j) & 1:
                current_sum += (n - count1[j]) * (1 << j)
            else:
                current_sum += count1[j] * (1 << j)
        if current_sum > max_sum:
            max_sum = current_sum
    
    results.append(str(max_sum))

print('\n'.join(results))
