t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    increasing = True

    for i in range(n-1):
        if a[i+1] < a[i]:
            increasing = False
            break

    if increasing:
        print(n)
    else:
        print(1)