import sys
from collections import Counter

input = sys.stdin.read


input_data = input().split()

t = int(input_data[0])
idx = 1
results = []

for _ in range(t):
    n = int(input_data[idx])
    a = input_data[idx + 1 : idx + 1 + n]
    idx += 1 + n

    cnt = Counter(a)
    found = -1
    for key, value in cnt.items():
        if value >= 3:
            found = key
            break
    
    results.append(str(found))
sys.stdout.write('\n'.join(results) + '\n')

