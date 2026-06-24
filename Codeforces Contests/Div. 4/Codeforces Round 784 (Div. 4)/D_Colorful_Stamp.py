t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    parts = s.split('W')
    ok = True

    for p in parts:
        if p == "":
            continue

        if 'B' not in p or 'R' not in p:
            ok = False
            break

    print("YES" if ok else "NO")