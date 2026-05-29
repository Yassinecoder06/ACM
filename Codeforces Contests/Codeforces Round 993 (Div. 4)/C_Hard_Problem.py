t = int(input())

for _ in range(t):
    m,a,b,c = map(int, input().split())

    row1 = min(a,m)
    row2 = min(b,m)

    rest = 2*m - row1 - row2

    r = min(c, rest)

    print(row1+row2+r)