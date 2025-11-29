import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # Step 1: check if arithmetic progression
    d = a[0] - a[1]
    ok = True
    for i in range(n - 1):
        if a[i] - a[i + 1] != d:
            ok = False
            break

    if not ok:
        print("NO")
        continue

    # Step 2: compute x and y
    numerator = a[0] - d * n
    denom = n + 1

    if numerator % denom != 0:
        print("NO")
        continue

    x = numerator // denom
    y = x + d

    if x >= 0 and y >= 0:
        print("YES")
    else:
        print("NO")

