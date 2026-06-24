t = int(input())

for _ in range(t):
    n = int(input())

    s = list(map(int, input().split()))
    s2 = s.copy()
    s2.sort()
    max1 = s2[-1]
    max2 = s2[-2]

    for i in range(n):
        if s[i] == max1:
            s[i] -= max2
        else:
            s[i] -= max1
    
    s = map(str, s)
    print(' '.join(s))