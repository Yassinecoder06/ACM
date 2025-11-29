from math import floor

def apply_cycle(x, s):
    for c in s:
        if c == "A":
            x -= 1
        else:
            x //= 2
        if x == 0:
            return 0
    return x

def apply_prefix(x, s, k):
    for i in range(k):
        if s[i] == "A":
            x -= 1
        else:
            x //= 2
        if x == 0:
            return 0
    return x

t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    s = input().strip()
    arr = list(map(int, input().split()))

    # Precompute cycle effects for 2^i cycles
    MAXP = 35  # 2^35 > 10^10, enough
    lifts = [dict() for _ in range(MAXP)]

    # lifts[0][x] = apply 1 cycle
    # But x ranges to 1e9 → cannot store all x
    # We compute lazily: only when needed.

    def cycle_lift(x, p):
        """Compute apply 2^p cycles to x, with memo."""
        if x == 0:
            return 0
        if x in lifts[p]:
            return lifts[p][x]
        if p == 0:
            res = apply_cycle(x, s)
        else:
            mid = cycle_lift(x, p - 1)
            res = cycle_lift(mid, p - 1)
        lifts[p][x] = res
        return res

    def can_with(times, s, a):
        if a == 0:
            return True

        full = times // n
        rem = times % n
        x = a
        
        # apply full cycles using lifting
        bit = 0
        while full > 0:
            if full & 1:
                x = cycle_lift(x, bit)
                if x == 0:
                    return True
            full >>= 1
            bit += 1

        # apply remainder steps
        x = apply_prefix(x, s, rem)
        return x == 0

    # Answer each query
    for a in arr:
        low, high = 1, 2 * a  # safe upper bound
        while low < high:
            mid = (low + high) // 2
            if can_with(mid, s, a):
                high = mid
            else:
                low = mid + 1
        print(low)
