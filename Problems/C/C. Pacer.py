t = int(input())
for i in range(t):
    n,m = map(int, input().split())
    a = []
    b = []
    path = [0]*m
    for j in range(n):
        a[j], b[j] = map(int, input().split())

    path[a[j]] = b[j]