from math import ceil
t = int(input())

for _ in range(t):
    x,y,k = map(int, input().split())

    dx = ceil(x/k)
    dy = ceil(y/k)
    if dx == dy:
        print(dx * 2)  
    elif max(dx, dy) == dy:
        print(max(dx, dy) * 2)
    else:
        print(max(dx, dy) * 2 - 1)