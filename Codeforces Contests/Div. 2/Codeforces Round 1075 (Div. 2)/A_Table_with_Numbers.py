
t = int(input())

for _ in range(t):
    n, h, l = map(int, input().split())
    a = list(map(int, input().split()))

    low = min(h, l)
    high = max(h, l)

    both = 0
    one_side = 0

    for x in a:
        if x <= low:
            both += 1
        elif x <= high:
            one_side += 1

    ans = min(both, (both + one_side) // 2)
    print(ans)