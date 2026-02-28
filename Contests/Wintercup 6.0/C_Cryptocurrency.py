t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    maximus = []
    maxi = 0

    for i in range(n-1):
        if a[i+1] - a[i] > 0:
            maxi += a[i+1] - a[i]
        else:
            maximus.append(maxi)
            maxi = 0

    maximus.append(maxi)

    print(max(maximus))