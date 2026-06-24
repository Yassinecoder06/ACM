t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    strings = []
    results = []

    for _ in range(n):
        strings.append(input())
    
    for i in range(n):
        for j in range(i+1, n):
            result = 0
            for k in range(m):
                result+=abs(ord(strings[i][k]) - ord(strings[j][k]))
            results.append(result)

    print(min(results))
    
