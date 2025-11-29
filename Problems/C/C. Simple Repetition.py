import sys
input = sys.stdin.readline

# Deterministic Miller–Rabin for n < 2^64
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    # small primes for quick screening
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29):
        if n == p:
            return True
        if n % p == 0:
            return False

    # write n-1 = d * 2^s
    d, s = n - 1, 0
    while d & 1 == 0:
        d //= 2
        s += 1

    # these bases suffice for determinism < 2^64
    bases = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)
    for a in bases:
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def run():
    t = int(input())
    for _ in range(t):
        x, k = input().split()
        k = int(k)

        # Fast composite‐by‐concatenation check:
        if k > 1 and x != "1":
            print("NO")
            continue

        # Build the number we actually need to test:
        if k == 1:
            y = int(x)
        else:
            # repunit of length k: (10^k - 1) // 9
            y = (10**k - 1) // 9

        print("YES" if is_prime(y) else "NO")


run()
