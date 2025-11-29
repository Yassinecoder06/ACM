import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    result = []

    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[n - i - 1]

    max_from_right = [0] * n
    max_from_right[0] = a[0]
    for i in range(1, n):
        max_from_right[i] = max(max_from_right[i - 1], a[i])

    for i in range(n):
        result.append(str(s[i] + max_from_right[n - i - 1]))

    print(" ".join(result))

#Accepted