from collections import Counter
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    current_sum = 0
    max_val = 0
    result = 0
    for i in range(n):
        current_sum += a[i]
        if a[i] > max_val:
            max_val = a[i]
        
        if 2 * max_val == current_sum:
            result += 1

    print(result)