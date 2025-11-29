t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    prefix_min = [a[0]] * (n)
    for i in range(1,n):
        prefix_min[i] = min(prefix_min[i-1], a[i])

    print(prefix_min[0] + prefix_min[1])

#Accepted