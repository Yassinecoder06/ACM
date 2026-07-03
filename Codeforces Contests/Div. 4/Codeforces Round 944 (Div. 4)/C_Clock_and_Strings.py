t = int(input())

for _ in range(t):
    a,b,c,d = map(int, input().split())

    x = sorted([a, b])
    y = sorted([c, d])

    start, end = x[0], x[1]
    
    c_inside = start < c < end
    d_inside = start < d < end
    
    if c_inside != d_inside:
        print('YES')
    else:
        print('NO')

