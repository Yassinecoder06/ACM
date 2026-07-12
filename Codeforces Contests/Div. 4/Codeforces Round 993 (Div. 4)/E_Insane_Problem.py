from math import floor, log
t = int(input())

for _ in range(t):
    k,l1,r1,l2,r2 = map(int, input().split())

    total_count = 0
    p = 1
    while p <= r2:
        low = (l2 + p - 1) // p
        high = r2 // p

        start = max(l1, low)
        end = min(r1, high)

        if start <= end:
            total_count += (end - start + 1)

        p *= k
    print(total_count)