
t = int(input())
out_lines = []
for _ in range(t):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    if n == 1 or k == n:
        out_lines.append("0")
        continue
    diffs = [abs(a[i] - a[i + 1]) for i in range(n - 1)]
    total = sum(diffs)
    diffs.sort(reverse=True)
    removed = sum(diffs[: k - 1])
    out_lines.append(str(total - removed))

print("\n".join(out_lines))
