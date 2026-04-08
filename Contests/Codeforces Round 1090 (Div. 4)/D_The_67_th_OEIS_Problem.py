import sys

def build_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            start = i * i
            step = i
            sieve[start : limit + 1 : step] = [False] * (((limit - start) // step) + 1)
    return [i for i in range(2, limit + 1) if sieve[i]]


t = int(input())
out = []
primes = build_primes(110000)
for _ in range(t):
    n = int(input())

    seq = []
    for i in range(n):
        seq.append(str(primes[i] * primes[i + 1]))
    out.append(" ".join(seq))
sys.stdout.write("\n".join(out))