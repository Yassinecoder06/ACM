import bisect
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    t_str = input_data[ptr]
    ptr += 1
    t = int(t_str)
    
    output = []
    for _ in range(t):
        n = int(input_data[ptr])
        q = int(input_data[ptr+1])
        ptr += 2
        
        a = []
        for _ in range(n):
            a.append(int(input_data[ptr]))
            ptr += 1
            
        k = []
        for _ in range(q):
            k.append(int(input_data[ptr]))
            ptr += 1
            
        prefix_sum = [0] * (n + 1)
        max_step = [0] * n
        
        current_max = 0
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + a[i]
            current_max = max(current_max, a[i])
            max_step[i] = current_max
            
        results = []
        for query in k:
            idx = bisect.bisect_right(max_step, query)
            results.append(str(prefix_sum[idx]))
            
        output.append(' '.join(results))
        
    sys.stdout.write('\n'.join(output) + '\n')

solve()
