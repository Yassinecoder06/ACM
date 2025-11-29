def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        n, q = map(int, data[index:index+2])
        index += 2
        a = data[index]
        b = data[index+1]
        index += 2
        
        # Precompute prefix frequency arrays
        freq_a = [[0] * 26 for _ in range(n + 1)]
        freq_b = [[0] * 26 for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(26):
                freq_a[i][j] = freq_a[i-1][j]
                freq_b[i][j] = freq_b[i-1][j]
            freq_a[i][ord(a[i-1]) - ord('a')] += 1
            freq_b[i][ord(b[i-1]) - ord('a')] += 1
        
        # Process each query
        for _ in range(q):
            l, r = map(int, data[index:index+2])
            index += 2
            
            # Compute character frequencies in range [l, r]
            freq_diff = [0] * 26
            for j in range(26):
                freq_a_lr = freq_a[r][j] - freq_a[l-1][j]
                freq_b_lr = freq_b[r][j] - freq_b[l-1][j]
                freq_diff[j] = abs(freq_a_lr - freq_b_lr)
            
            # Calculate minimum operations
            results.append(sum(freq_diff) // 2)
    
    # Output result
    sys.stdout.write("\n".join(map(str, results)) + "\n")

solve()

