t = int(input())

for _ in range(t):
    n = int(input())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    d = []
    for i in range(n):
        d.append(b[i] - a[i])

    possible = True
    current_surplus = 0
    for i in range(n):
        current_surplus += d[i]
        if current_surplus < 0:
            possible = False
            break
    
    if possible:
        print('YES')
    else:
        print('NO')
