from math import ceil
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    abs_a = list(abs(x) for x in a)
    rang_of_a0 = 1
    for i in range(1,n):
        if abs_a[i] > abs_a[0]:
            rang_of_a0 += 1

    if ceil(n/2) <= rang_of_a0:
        print("YES")
    else:
        print("NO")

#Accepted