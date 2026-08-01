t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    mx = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] > mx:
                mx = a[i][j]

    row_cnt = [0] * n
    col_cnt = [0] * m
    total = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == mx:
                row_cnt[i] += 1
                col_cnt[j] += 1
                total += 1

    flag = 0
    for i in range(n):
        for j in range(m):
            if row_cnt[i] + col_cnt[j] - (1 if a[i][j] == mx else 0) == total:
                flag = 1
                break
        if flag:
            break

    print(mx - flag)