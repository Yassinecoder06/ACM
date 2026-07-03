from collections import Counter
import sys

input_data = sys.stdin.read().split()


    
t = int(input_data[0])
ptr = 1
results = []

TARGET = (1 << 31) - 1

for _ in range(t):
    n = int(input_data[ptr])
    ptr += 1
    a = list(map(int, input_data[ptr : ptr + n]))
    ptr += n
    
    zeros = []
    ones = []
    for x in a:
        if x & (1 << 30):
            ones.append(x)
        else:
            zeros.append(x)
    
    one_counts = Counter(ones)
    pairs = 0
    
    for x in zeros:
        complement = TARGET - x
        if one_counts[complement] > 0:
            pairs += 1
            one_counts[complement] -= 1

    results.append(str(n - pairs))

sys.stdout.write("\n".join(results) + "\n")






