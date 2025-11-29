def solve():
    n = int(input())
    a = list(map(int, input().split()))

    perimetre = sum(a)
    if perimetre % 2 != 0:
        print("0")
        return 

    arc_diametre = perimetre // 2
    triangles = 0

    prefix_sum = [0] * (n+1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + a[i]

    i = 0
    j = 1

    while j < n and i < n - 1:
        arc = prefix_sum[j] - prefix_sum[i]
        if arc == arc_diametre:
            triangles += (n-2)
            i += 1
            j += 1
        elif arc > arc_diametre:
            i += 1
        else:
            j += 1
        
    print(triangles)

solve()