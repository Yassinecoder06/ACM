import sys
from collections import Counter

input_data = sys.stdin.read().split()

ptr = 0
t = int(input_data[ptr])
ptr += 1

results = []
for _ in range(t):
    n = int(input_data[ptr])
    k = int(input_data[ptr+1])
    ptr += 2
    a = list(map(int, input_data[ptr : ptr + n]))
    ptr += n
    
    sorted_c = [count for _, count in Counter(a).most_common()]
    m = len(sorted_c)
    ans = 0
    sum_S = 0
    for p in range(1, m + 1):
        sum_S += sorted_c[p-1]
        if (k - sum_S) % p == 0:
            d = (k - sum_S) // p
            x_min = sorted_c[p] if p < m else 0
            x_max = sorted_c[p-1] - 1
            if max(x_min, -d) <= x_max:
                ans += 1
    results.append(str(ans))
    
sys.stdout.write("\n".join(results) + "\n")

