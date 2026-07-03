t = int(input())

MAX_N = 200000

memo = [0] * (MAX_N + 1)
for i in range(1,MAX_N+1):
    memo[i] = 1 + memo[i//3]

prefix_sum = [0] * (MAX_N + 1)
for i in range(1, MAX_N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + memo[i]

for _ in range(t):
    l,r = map(int, input().split())
    print(memo[l] + prefix_sum[r] - prefix_sum[l-1])
        