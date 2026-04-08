t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):
        minimum = min(a[:i+1])
        maximum = max(a[i:])
        if a[i] == minimum or a[i] == maximum:
            count +=1
    print(count)