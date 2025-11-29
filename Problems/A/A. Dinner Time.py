t = int(input())
for _ in range(t):
    n,m,p,q = map(int, input().split())
    k = n // p
    if (k*p + 1 > n):
        if (k*q == m):
            print("YES")
        else:
            print("NO")
    else:
        print("YES")

#Accepted