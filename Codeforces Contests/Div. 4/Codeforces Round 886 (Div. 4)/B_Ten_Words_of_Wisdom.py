t = int(input())
for _ in range(t):
    n = int(input())
    result = []
    for i in range(n):
        x,y = map(int, input().split())
        if x > 10:
            continue
        result.append((y,i+1))

    m = max(result, key=lambda x:x[0])
    print(m[1])