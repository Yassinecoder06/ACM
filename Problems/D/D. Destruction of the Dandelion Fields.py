from math import floor
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    c = []
    result = 0
    for i in range(n):
        if a[i]%2==0:
            b.append(a[i])
        else:
            c.append(a[i])
    c.sort()
    if c:
        result += sum(b)
        result += sum(c[floor(len(c)//2):]) 
    print(result)
