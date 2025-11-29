t = int(input())
for _ in range(t):
    n,x = map(int, input().split())
    result = []
    for i in range(n):
        if i != x:
            result.append(str(i))
    if len(result) < n : result.append(str(x))
    print(" ".join(result))

#Accepted