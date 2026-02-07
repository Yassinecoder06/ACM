import bisect

n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))

prefix_sum = [0] * (n+1)
for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + a[i]

for j in q:
    print(bisect.bisect_left(prefix_sum, j))