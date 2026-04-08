import sys
t = int(input())
out = []
for _ in range(t):
    n,q = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [a[i] if a[i] > b[i] else b[i] for i in range(n)]

    for i in range(n - 2, -1, -1):
        if c[i] < c[i + 1]:
            c[i] = c[i + 1]

    prefix_sum = [0]*(n+1)

    for i in range(1,n+1):
        prefix_sum[i] = prefix_sum[i-1] + c[i-1]

    output = []

    for _ in range(q):
        l,r = map(int, input().split())
        output.append(str(prefix_sum[r] - prefix_sum[l-1]))

    out.append(" ".join(output))

sys.stdout.write("\n".join(out))