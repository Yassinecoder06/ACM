MOD = 10**9 + 7

M = int(input())

# dp[n] = number of partitions of n into distinct positive integers
dp = [0] * (M + 1)
dp[0] = 1  # base case: empty sum

for k in range(1, M + 1):
    for n in range(M, k - 1, -1):
        dp[n] = (dp[n] + dp[n - k]) % MOD

# count bitonic sequences
res = [0] * (M + 1)
for N in range(1, M + 1):
    total = 0
    for peak in range(1, N + 1):
        s = N - peak
        total = (total + dp[s] * dp[s]) % MOD
    res[N] = total

print(" ".join(str(res[i]) for i in range(1, M + 1)))
