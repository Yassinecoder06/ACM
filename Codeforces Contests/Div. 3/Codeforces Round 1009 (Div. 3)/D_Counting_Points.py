from math import isqrt
import sys


data = list(map(int, sys.stdin.buffer.read().split()))
it = iter(data)
t = next(it)
out = []

for _ in range(t):
    n = next(it)
    m = next(it)
    x = [next(it) for _ in range(n)]
    r = [next(it) for _ in range(n)]

    best = {}
    best_get = best.get

    for center, radius in zip(x, r):
        rr = radius * radius
        for dx in range(-radius, radius + 1):
            y = isqrt(rr - dx * dx)
            pos = center + dx
            prev = best_get(pos)
            if prev is None or y > prev:
                best[pos] = y

    ans = 0
    for y in best.values():
        ans += 2 * y + 1

    out.append(str(ans))

sys.stdout.write("\n".join(out))

    

