import sys

input = sys.stdin.read
data = input().split()

iterator = iter(data)
t = int(next(iterator))
out = []

for _ in range(t):
    n = int(next(iterator))
    seen = [False] * (n + 1)
    a = []

    for _ in range(n):
        x = int(next(iterator))
        if not seen[x]:
            seen[x] = True
            a.append(x)

    res = [str(x) for x in a]
    for i in range(1, n + 1):
        if not seen[i]:
            res.append(str(i))

    out.append(" ".join(res))
    
sys.stdout.write('\n'.join(out) + '\n')