t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()
    count = 0
    a = a[::-1]
    length = 1

    for j in range(n):
        if a[j] * length >= x:
            count += 1
            length = 1
        else:
            length += 1

    print(count)
