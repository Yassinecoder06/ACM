t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    data = {-1: 0, 0: 0, 1: 0}

    for i in range(n):
        data[a[i]] += 1
    
    result = 0
    if data[-1] % 2 == 1:
        result +=2
    result += data[0]
    print(result)
