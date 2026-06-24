t = int(input())

for _ in range(t):
    n = int(input())
    m = {}
    for _ in range(n):
        x,y = input().split()

        m[int(y,2)] = min(m.get(int(y,2), float('inf')), int(x))
    

    case1 = m.get(3, float('inf'))
    case2 = m.get(1, float('inf')) + m.get(2, float('inf'))
    result = min(case1, case2)
    if result == float('inf'):
        print(-1)
    else:
        print(result)