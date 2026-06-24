t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    q = [str(n-p[i] + 1) for i in range(n)]

    print(" ".join(q))
