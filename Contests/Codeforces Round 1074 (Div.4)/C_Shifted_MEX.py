def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    max_mex = 0
    
    # Try each element as the starting point (shift it to 0)
    for i in range(n):
        x = -a[i]
        shifted_set = set(a[j] + x for j in range(n))
        
        # Find MEX of the shifted array
        mex = 0
        while mex in shifted_set:
            mex += 1
        
        max_mex = max(max_mex, mex)
    
    return max_mex

t = int(input())
for _ in range(t):
    print(solve())
