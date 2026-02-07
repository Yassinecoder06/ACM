t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    results = []
    result = 0
    increasing = False
    for i in range(1,n):
        if a[i] > a[i-1]:
            result += (a[i] - a[i-1])

        else:
            results.append(result) 
            result = 0
    results.append(result)

    print(max(results))