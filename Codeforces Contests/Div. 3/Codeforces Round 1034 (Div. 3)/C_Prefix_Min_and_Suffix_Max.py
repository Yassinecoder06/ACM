t = int(input())

for _ in range(t):
    n = int(input())

    a = list(map(int, input().split()))

    prefix_min = [0] * n
    prefix_min[0] = a[0]
    for i in range(1, n):
        prefix_min[i] = min(prefix_min[i-1], a[i])

    suffix_max = [0] * n
    suffix_max[n-1] = a[n-1]
    for i in range(n-2, -1, -1):
        suffix_max[i] = max(suffix_max[i+1], a[i])

    result = []
    for i in range(n):
        if a[i] == prefix_min[i] or a[i] == suffix_max[i]:
            result.append('1')
        else:
            result.append('0')

    print(''.join(result))