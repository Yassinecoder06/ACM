t = int(input())
out = []

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    pairs = [[a[0], 1]]
    for i in range(1, n):
        if a[i] == a[i - 1]:
            pairs[-1][1] += 1
        else:
            pairs.append([a[i], 1])

    ok = False
    while pairs:
        m = len(pairs)
        if pairs[-1][1] % 2 == 0:
            ok = True
            break
        if m == 1:
            break
        if pairs[-1][0] - pairs[-2][0] <= k:
            ok = True
            break
        pairs.pop()

    out.append("YES" if ok else "NO")

print('\n'.join(out))
