import sys

data = list(map(int, sys.stdin.buffer.read().split()))
ptr = 0

t = data[ptr]
ptr += 1

ans = []

for _ in range(t):
    n = data[ptr]
    ptr += 1

    seen = {0}
    add = seen.add

    pref = 0
    sign = 1
    ok = False

    for _ in range(n):
        pref += sign * data[ptr]
        ptr += 1
        sign = -sign

        if pref in seen:
            ok = True
            ptr += n - _ - 1
            break

        add(pref)

    ans.append("YES" if ok else "NO")

sys.stdout.write("\n".join(ans))