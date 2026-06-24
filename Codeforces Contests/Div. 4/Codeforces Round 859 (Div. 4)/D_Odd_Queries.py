t = int(input())

for _ in range(t):
    n,q = map(int, input().split())

    a = list(map(int, input().split()))

    prefix_sum = [0] * (n+1)
    for i in range(1, n+1):
        prefix_sum[i] = prefix_sum[i-1] + a[i-1]

    for _ in range(q):
        l,r,k = map(int, input().split())

        s = prefix_sum[-1] - (prefix_sum[r] - prefix_sum[l-1]) + (r-l+1)*k
        if s % 2==1:
            print('YES')
        else:
            print('NO')