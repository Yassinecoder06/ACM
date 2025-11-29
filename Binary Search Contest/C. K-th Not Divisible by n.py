from math import ceil

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())

    
    x = ceil(k / (n - 1))


    j = k + (x - 1)

    print(j)
