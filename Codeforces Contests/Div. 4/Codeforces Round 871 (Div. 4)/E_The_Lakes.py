t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    vis = [[False] * m for _ in range(n)]
    ans = 0

    for i in range(n):
        for j in range(m):
            if a[i][j] > 0 and not vis[i][j]:
                stack = [(i, j)]
                vis[i][j] = True
                cur = 0

                while stack:
                    x, y = stack.pop()
                    cur += a[x][y]

                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx = x + dx
                        ny = y + dy

                        if (0 <= nx < n and
                            0 <= ny < m and
                            a[nx][ny] > 0 and
                            not vis[nx][ny]):

                            vis[nx][ny] = True
                            stack.append((nx, ny))

                ans = max(ans, cur)

    print(ans)