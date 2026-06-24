from collections import Counter
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n):
        m, b = input().split()
        m = int(m)

        cnt = Counter(b)
        a[i] = (a[i] - cnt['U'] + cnt['D']) % 10
        

    a = map(str, a)
    print(' '.join(a))