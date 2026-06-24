t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    b = list(map(int, input().split()))
    output = 1
    for i in range(n):
        output += max(0, a[i] - b[i])

    print(output)
