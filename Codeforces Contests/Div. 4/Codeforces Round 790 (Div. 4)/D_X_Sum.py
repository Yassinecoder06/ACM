t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    a = [list(map(int, input().split())) for _ in range(n)]

    diag1 = {}  
    diag2 = {}

    for i in range(n):
        for j in range(m):
            d1 = i - j
            d2 = i + j

            diag1[d1] = diag1.get(d1, 0) + a[i][j]
            diag2[d2] = diag2.get(d2, 0) + a[i][j]

    ans = 0

    # Try each cell as the center
    for i in range(n):
        for j in range(m):
            cur = diag1[i - j] + diag2[i + j] - a[i][j]
            ans = max(ans, cur)

    print(ans)