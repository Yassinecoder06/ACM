t = int(input())
results = []
for _ in range(t):
    n,m = map(int,input().split())
    r = -1
    c = -1
    mx = -1
    subtract = True
    for i in range(n):
        row = list(map(int, input().split()))
        m = max(row)
        if  m > mx:
            mx = m
            if row.count(m) > 1:
                r = i
            else:
                c = row.index(m)
            subtract = True
        elif m == mx:
            if row.count(m) > 1 and r == -1:
                r = i
            if row.count(m) == 1 and c == -1:
                c = row.index(m)

            if row.count(m) > 1 and r != i:
                subtract = False
            if row.count(m) == 1:
                if row.index(m) != c: 
                    subtract = False
    if subtract:
        results.append(mx - 1)
    else:
        results.append(mx)

for result in results: 
    print(result)
