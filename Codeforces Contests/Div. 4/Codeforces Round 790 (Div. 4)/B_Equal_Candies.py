t= int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    m = min(a)

    for i in range(n):
        a[i] -= m

    print(sum(a))