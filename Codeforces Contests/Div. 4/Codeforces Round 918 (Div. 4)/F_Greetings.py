import sys
from bisect import bisect_right

input_data = sys.stdin.read().split()
it = iter(input_data)
t_str = next(it, None)

t = int(t_str)
results = []
for _ in range(t):
    n = int(next(it))
    pairs = []
    for _ in range(n):
        a = int(next(it))
        b = int(next(it))
        pairs.append((a, b))
    pairs.sort(key=lambda x: x[1])
    
    a_coords = [p[0] for p in pairs]
    
    sorted_a = sorted(a_coords)
    rank = {val: i + 1 for i, val in enumerate(sorted_a)}
    
    bit = [0] * (n + 1)
    def update(idx, val):
        while idx <= n:
            bit[idx] += val
            idx += idx & (-idx)
    
    def query(idx):
        s = 0
        while idx > 0:
            s += bit[idx]
            idx -= idx & (-idx)
        return s
     
    count = 0
    for i in range(n):
        r = rank[a_coords[i]]
        count += i - query(r)
        update(r, 1)
    
    results.append(str(count))

sys.stdout.write("\n".join(results) + "\n")

