t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    parity = (a[0] % 2)
    
    for i in range(1,n):
        if a[i] % 2 != parity:
            a.sort()
            break
    
    a = list(map(str, a))
    print(" ".join(a))