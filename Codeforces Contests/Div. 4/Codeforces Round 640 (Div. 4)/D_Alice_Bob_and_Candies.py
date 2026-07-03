t = int(input())

for _ in range(t):
    n = int(input())

    a = list(map(int, input().split()))

    prefix_sum = [0] * (n+1)
    for i in range(1, n+1):
        prefix_sum[i] = prefix_sum[i-1] + a[i-1]


    suffix_sum = [0] * (n+1)
    for i in range(n, 0, -1):
        suffix_sum[i-1] = suffix_sum[i] + a[i-1]

    r = n
    a = 0
    b = 0
    s = 0
    moves = 0

    last_l = 0
    l = 0
    last_r = n
    r = n
    
    while l < r:
        if moves%2==0:
            if prefix_sum[l] - prefix_sum[last_l] <= s:
                l += 1
            else:
                s = prefix_sum[l] - prefix_sum[last_l]
                a += s
                last_l = l
                moves += 1
        else:
            if suffix_sum[r] - suffix_sum[last_r] <= s:
                r -= 1
            else:
                s = suffix_sum[r] - suffix_sum[last_r]
                b += s
                last_r = r
                moves += 1

    if moves%2==1 and a+b!=prefix_sum[-1]:
        s = suffix_sum[r] - suffix_sum[last_r]
        b += s
        moves += 1
    elif moves%2==0 and a+b!=prefix_sum[-1]:
        s = prefix_sum[l] - prefix_sum[last_l]
        a += s
        moves += 1
    
    print(moves, a, b)