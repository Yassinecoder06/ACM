t = int(input())

for _ in range(t):
    n = int(input())
    s = list(input().split())

    count_0 = 0
    count = 0

    for i in range(n):
        if s[i] == '1':
            count_0 = max(count_0, count)
            count = 0
            
        else:
            count += 1
    count_0 = max(count_0, count)

    print(count_0)
    