import sys

input = sys.stdin.readline


def build_prefix_stats(left_pos, right_pos):
    n = len(left_pos)
    inf = 10**9

    min_val = inf
    min_idx = -1
    min2 = inf

    max_val = -1
    max_idx = -1
    max2 = -1

    pref_min = [inf] * (n + 1)
    pref_min_idx = [-1] * (n + 1)
    pref_min2 = [inf] * (n + 1)

    pref_max = [-1] * (n + 1)
    pref_max_idx = [-1] * (n + 1)
    pref_max2 = [-1] * (n + 1)

    for k in range(n + 1):
        pref_min[k] = min_val
        pref_min_idx[k] = min_idx
        pref_min2[k] = min2

        pref_max[k] = max_val
        pref_max_idx[k] = max_idx
        pref_max2[k] = max2

        if k == n:
            break

        lv = left_pos[k]
        if lv < min_val:
            min2 = min_val
            min_val = lv
            min_idx = k
        elif lv < min2:
            min2 = lv

        rv = right_pos[k]
        if rv > max_val:
            max2 = max_val
            max_val = rv
            max_idx = k
        elif rv > max2:
            max2 = rv

    return pref_min, pref_min_idx, pref_min2, pref_max, pref_max_idx, pref_max2


def max_mex_even(L, R, pref_min, pref_max):
    n = len(pref_min) - 1
    lo = 0
    hi = n
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if pref_min[mid] >= L and pref_max[mid] <= R:
            lo = mid
        else:
            hi = mid - 1
    return lo


def max_mex_odd(
    L,
    R,
    center_value,
    pref_min,
    pref_min_idx,
    pref_min2,
    pref_max,
    pref_max_idx,
    pref_max2,
):
    n = len(pref_min) - 1
    lo = 0
    hi = n
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if center_value < mid:
            if pref_min_idx[mid] == center_value:
                min_val = pref_min2[mid]
            else:
                min_val = pref_min[mid]

            if pref_max_idx[mid] == center_value:
                max_val = pref_max2[mid]
            else:
                max_val = pref_max[mid]
        else:
            min_val = pref_min[mid]
            max_val = pref_max[mid]

        if min_val >= L and max_val <= R:
            lo = mid
        else:
            hi = mid - 1
    return lo


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = 2 * n

    first_pos = [-1] * n
    left_pos = [0] * n
    right_pos = [0] * n
    pair = [0] * m

    for i, v in enumerate(a):
        if first_pos[v] == -1:
            first_pos[v] = i
            left_pos[v] = i
        else:
            pair[i] = first_pos[v]
            pair[first_pos[v]] = i
            right_pos[v] = i

    mid_sum = [i + pair[i] for i in range(m)]

    run_left = [1] * m
    for i in range(1, m):
        if mid_sum[i] == mid_sum[i - 1]:
            run_left[i] = run_left[i - 1] + 1

    run_right = [1] * m
    for i in range(m - 2, -1, -1):
        if mid_sum[i] == mid_sum[i + 1]:
            run_right[i] = run_right[i + 1] + 1

    (
        pref_min,
        pref_min_idx,
        pref_min2,
        pref_max,
        pref_max_idx,
        pref_max2,
    ) = build_prefix_stats(left_pos, right_pos)

    answer = 0

    i = 0
    while i < m:
        j = i
        while j + 1 < m and mid_sum[j + 1] == mid_sum[i]:
            j += 1
        mex_val = max_mex_even(i, j, pref_min, pref_max)
        if mex_val > answer:
            answer = mex_val
        i = j + 1

    for c in range(m):
        target = 2 * c
        left_len = 0
        if c > 0 and mid_sum[c - 1] == target:
            left_len = run_left[c - 1]
        right_len = 0
        if c + 1 < m and mid_sum[c + 1] == target:
            right_len = run_right[c + 1]

        k = left_len if left_len < right_len else right_len
        L = c - k
        R = c + k

        mex_val = max_mex_odd(
            L,
            R,
            a[c],
            pref_min,
            pref_min_idx,
            pref_min2,
            pref_max,
            pref_max_idx,
            pref_max2,
        )
        if mex_val > answer:
            answer = mex_val

    print(answer)