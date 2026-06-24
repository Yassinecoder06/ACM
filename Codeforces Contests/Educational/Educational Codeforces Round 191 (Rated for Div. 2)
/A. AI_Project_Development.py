from math import ceil
t = int(input())

for _ in range(t):
    n,x,y,z = map(int, input().split())

    print((min(ceil(n/(x+y)), ceil(z+((n-x*z)/(x+10*y))))))