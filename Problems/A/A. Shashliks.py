from math import ceil
t = int(input())
for _ in range(t):
    k,a,b,x,y = map(int, input().split())
    s = 0
    if a > k and b > k:
        print(0)
    else:
        if x < y:
            s = ceil((k-a + 1) / x)
            k = k - s * x
            if k >= b: s += ceil((k-b +1) / y) 
        else:
            s = ceil((k-b + 1) / y)
            k = k - s * y
            if k >= a: s += ceil((k-a +1) / x) 
        print(s)