import bisect

n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
x  = a[k-1]+1
idx = bisect.bisect_right(a, x)

if k == n:
    print(-1)
elif idx == k:
    print(x)
else:
    print(-1)