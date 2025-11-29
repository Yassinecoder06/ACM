t = int(input())
for _ in range(t):
    n,s = map(int, input().split())
    x = list(map(int, input().split()))
    minimum = x[0]
    maximum = x[n-1]
    if minimum <= s <= maximum: print(min(s-minimum, maximum-s)*2 + max(s-minimum, maximum-s))
    elif minimum > s:
        print(maximum - s)
    elif s > maximum:
        print(s-minimum)