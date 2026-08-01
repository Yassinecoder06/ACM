import sys

data = list(map(int, sys.stdin.buffer.read().split()))
it = iter(data)
t = next(it)
out = []
for _ in range(t):
    n = next(it)
    m = next(it)
    a = [0] + [next(it) for _ in range(n)]
    posts = [next(it) for _ in range(m)]
    pref = [0] * (n + 1)
    for i in range(1, n + 1):
        pref[i] = pref[i - 1] + a[i]
        
    dp_neg = 0
    dp_pos = -10**30
    for p in sorted(posts, reverse=True):
        x = pref[p]
        next_neg = max(dp_neg, dp_pos + x)
        next_pos = max(dp_pos, dp_neg - x)
        dp_neg, dp_pos = next_neg, next_pos
    out.append(str(pref[-1] + 2 * max(dp_neg, dp_pos)))

sys.stdout.write("\n".join(out))

