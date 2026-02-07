import bisect

n = int(input())
x = sorted(map(int, input().split())) 
q = int(input())

for _ in range(q):
    m = int(input())

    c = bisect.bisect_right(x, m)
    print(c)
