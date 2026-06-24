from collections import Counter
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    cnt = Counter(a)
    u = len(cnt)

    if (n - u) % 2 == 1:
        print(u - 1)
    else:
        print(u)