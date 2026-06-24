t = int(input())

for _ in range(t):
    a = list(map(int, input().split()))

    s = a[0]

    a.sort()
    print(3-a.index(s))

