t = int(input())
for _ in range(t):
    n,m,l,r = map(int, input().split())
    l1 = r1 = 0
    for i in range(r+1):
        r1 = i
        l1 = -m + r1
        if l<=l1<=0:
            break
    print(l1,r1)