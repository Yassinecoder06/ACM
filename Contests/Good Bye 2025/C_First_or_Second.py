import sys

def solve():
    # Fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    try:
        num_test_cases = int(next(iterator))
    except StopIteration:
        return
        
    results = []
    
    for _ in range(num_test_cases):
        try:
            n = int(next(iterator))
            a = [int(next(iterator)) for _ in range(n)]
        except StopIteration:
            break
            
        # Precompute suffix sums
        # suff[i] = sum(a[i:])
        suff = [0] * (n + 1)
        current_suff = 0
        for i in range(n - 1, -1, -1):
            current_suff += a[i]
            suff[i] = current_suff
            
        # Case k=0: Survivor is a[0]
        # All other elements a[1]...a[n-1] are removed as 'second'
        # Contribution is -sum(a[1:])
        max_x = -suff[1]
        
        # Case k > 0: Survivor is a[k]
        # a[0] is always removed as 'first' -> +a[0]
        # a[1]...a[k-1] can be removed as 'first' or 'second' -> +|a[i]|
        # a[k+1]...a[n-1] are always removed as 'second' -> -a[j]
        
        prefix_abs_sum = 0
        base_val = a[0]
        
        for k in range(1, n):
            # Update prefix_abs_sum for a[k-1]
            if k > 1:
                prefix_abs_sum += abs(a[k-1])
            
            # Calculate X for survivor k
            # X = a[0] + sum(|a[1]...a[k-1]|) - sum(a[k+1]...a[n-1])
            current_x = base_val + prefix_abs_sum - suff[k+1]
            
            if current_x > max_x:
                max_x = current_x
                
        results.append(str(max_x))
        
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()
