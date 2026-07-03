t = int(input())

for _ in range(t):
    a = list(map(list, input().split()))

    a[0][0], a[1][0] = a[1][0], a[0][0]

    a = map(''.join, a)
    print(' '.join(a))