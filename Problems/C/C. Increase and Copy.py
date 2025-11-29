t = int(input())

for _ in range(t):
    n = int(input())

    low, high = 0, 2 * int(1e5)

    while low < high:
        mid = (low + high) // 2
        i = mid // 2
        max_sum = (i + 1) * (mid - i + 1)

        if max_sum >= n:
            high = mid
        else:
            low = mid + 1

    print(low)

