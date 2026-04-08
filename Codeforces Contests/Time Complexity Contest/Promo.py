n, q = map(int, input().split())
l = list(map(int, input().split()))
l.sort()

prefix_sum = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + l[i - 1]

for _ in range(q):
    x, y = map(int, input().split())
    print(prefix_sum[n-x+y] - prefix_sum[n-x])

