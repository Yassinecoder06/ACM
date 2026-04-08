import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    ok = [0] * n
    for i in range(1, n):
        if a[i] > a[i - 1] / 2:
            ok[i] = 1
    

    cur = sum(ok[1:k+1])   
    count = 0
    for i in range(1, n - k + 1):
        if cur == k:       
            count += 1
        
        if i + k < n: 
            cur = cur + ok[i + k] - ok[i]
    print(count)
