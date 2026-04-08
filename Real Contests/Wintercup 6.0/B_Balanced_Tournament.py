def solve():
    import sys
    input = sys.stdin.readline
    
    T = int(input())
    
    for _ in range(T):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        
        if n == 1:
            print(0)
            continue
        
        arr.sort()
        
        # Initial difference without any potion
        ans = arr[-1] - arr[0]
        
        for i in range(1, n):
            # Max power after adjustment
            high = max(arr[i-1] + k, arr[-1] - k)
            
            # Min power after adjustment
            low = min(arr[0] + k, arr[i] - k)
            
            ans = min(ans, high - low)
        
        print(ans)

solve()