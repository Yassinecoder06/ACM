from sys import stdin
input = stdin.readline

def build_prefix_counts(s):
    n = len(s)
    prefA = [0] * (n + 1)
    prefB = [0] * (n + 1)
    for i, ch in enumerate(s):
        prefA[i+1] = prefA[i] + (1 if ch == 'A' else 0)
        prefB[i+1] = prefB[i] + (1 if ch != 'A' else 0)
    return prefA, prefB

def total_counts_in_first_k(k, n, A_per_cycle, B_per_cycle, prefA, prefB):
    # number of full cycles
    full = k // n
    rem = k % n
    totalA = full * A_per_cycle + prefA[rem]
    totalB = full * B_per_cycle + prefB[rem]
    return totalA, totalB

def becomes_zero_within_steps(x, steps, n, A_cycle, B_cycle, prefA, prefB):
    """
    Return True if starting from x, applying 'steps' first operations (s repeated) makes number == 0.
    This preserves the order of ops.
    """
    if x == 0:
        return True

    # quick case: no B at all -> only A's (decrements)
    if B_cycle == 0:
        totalA, _ = total_counts_in_first_k(steps, n, A_cycle, B_cycle, prefA, prefB)
        return x <= totalA

    # quick case: if total B in first `steps` >= 60, we know it's zero
    _, totalB = total_counts_in_first_k(steps, n, A_cycle, B_cycle, prefA, prefB)
    if totalB >= 60:
        return True

    # Otherwise totalB < 60 => simulate step-by-step (bounded simulation)
    number = x
    # To avoid iterating up to huge `steps`, we iterate but will stop:
    # - when number == 0
    # - or after `steps` steps
    # Because totalB < 60, the number of halvings is < 60, so simulation will be short in practice.
    for i in range(steps):
        ch = s[i % n]
        if ch == 'A':
            number -= 1
        else:
            number //= 2
        if number == 0:
            return True
    return number == 0


t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    s = input().strip()
    arr = list(map(int, input().split()))

    prefA, prefB = build_prefix_counts(s)
    A_cycle = prefA[-1]
    B_cycle = prefB[-1]

    # binary search upper bound on steps: keep large enough (problem used 1e9)
    MAX_STEPS = 10**18  # safe upper bound if needed

    for x in arr:
        lo, hi = 0, MAX_STEPS
        while lo < hi:
            mid = (lo + hi) // 2
            if becomes_zero_within_steps(x, mid, n, A_cycle, B_cycle, prefA, prefB):
                hi = mid
            else:
                lo = mid + 1
        print(lo)
