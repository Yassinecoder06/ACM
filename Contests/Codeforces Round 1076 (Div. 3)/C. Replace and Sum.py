import sys

data = sys.stdin.read().split()

index = 0
t = int(data[index])
index += 1
for _ in range(t):
    n = int(data[index])
    q = int(data[index + 1])
    index += 2
    a = [int(x) for x in data[index:index + n]]
    index += n
    b = [int(x) for x in data[index:index + n]]
    index += n
    
    # build sparse table for b
    logn = 0
    while (1 << logn) <= n:
        logn += 1
    st = [[0] * logn for _ in range(n)]
    for i in range(n):
        st[i][0] = b[i]
    for j in range(1, logn):
        for i in range(n - (1 << j) + 1):
            st[i][j] = max(st[i][j - 1], st[i + (1 << (j - 1))][j - 1])
    
    def query_max(l, r):
        if l > r:
            return 0
        k = 0
        while (1 << (k + 1)) <= r - l + 1:
            k += 1
        return max(st[l][k], st[r - (1 << k) + 1][k])
    
    # now, for each query
    answers = []
    for __ in range(q):
        l = int(data[index]) - 1
        r = int(data[index + 1]) - 1
        index += 2
        s = a[r]
        # binary search for p
        low = l
        high = r
        while low <= high:
            mid = (low + high) // 2
            if query_max(mid, n-1) > s:
                low = mid + 1
            else:
                high = mid - 1
        p = high
        if p < l or query_max(p, n-1) <= s:
            p = l - 1
        # now, compute sum
        total = 0
        if p >= l:
            # sum from i=l to p m_i
            current_m = query_max(p, n-1)
            total += current_m
            for i in range(p - 1, l - 1, -1):
                current_m = max(b[i], current_m)
                total += current_m
        # then, for i=p+1 to r, add s
        num = r - (p + 1) + 1
        if num > 0:
            total += s * num
        answers.append(str(total))
    print(' '.join(answers))

