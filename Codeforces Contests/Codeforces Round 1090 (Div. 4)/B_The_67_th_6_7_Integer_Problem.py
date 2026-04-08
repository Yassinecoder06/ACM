t = int(input())

for _ in range(t):
    a = list(map(int, input().split()))
    n = 7

    a.sort()

    for i in range(n-1):
        a[i] *= -1


    print(sum(a))