t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    ans = 0
    pos = 0
    last = 0

    for _ in range(n):
        a, b = map(int, input().split())
        d = a - last

        if pos == b:
            ans += (d // 2) * 2
        else:
            ans += ((d-1) // 2) * 2 + 1

        pos = b
        last = a
    add = m - last

    print(ans +add)