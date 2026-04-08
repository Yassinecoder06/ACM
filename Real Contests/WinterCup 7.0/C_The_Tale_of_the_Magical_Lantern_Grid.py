import sys
input = sys.stdin.readline
MOD = 10**9 + 7
MAXN = 10**5

# Step 1: Compute mobius function μ(n) using sieve
mu = [1] * (MAXN + 1)
is_prime = [True] * (MAXN + 1)
primes = []

for i in range(2, MAXN + 1):
    if is_prime[i]:
        primes.append(i)
        mu[i] = -1
    for p in primes:
        if i * p > MAXN:
            break
        is_prime[i * p] = False
        if i % p == 0:
            mu[i * p] = 0
            break
        else:
            mu[i * p] = -mu[i]

# Step 2: Process test cases
t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0

    for d in range(1, n + 1):
        if mu[d] == 0:
            continue
        k = n // d
        s = k * (k + 1) // 2 % MOD
        term = mu[d] * d * d % MOD * s * s % MOD
        ans = (ans + term) % MOD

    print(ans)