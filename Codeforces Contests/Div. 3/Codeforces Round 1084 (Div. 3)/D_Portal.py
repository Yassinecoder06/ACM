import sys

input = sys.stdin.readline
t = int(input())
ans = []
for _ in range(t):
    n, x, y = map(int, input().split())
    p = list(map(int, input().split()))
    inside = p[x:y]
    outside = p[:x] + p[y:]
    mn = min(inside)
    pos = inside.index(mn)
    inside = inside[pos:] + inside[:pos]
    insert_at = 0
    while insert_at < len(outside) and outside[insert_at] < mn:
        insert_at += 1
    res = outside[:insert_at] + inside + outside[insert_at:]
    ans.append(" ".join(map(str, res)))
print("\n".join(ans))
