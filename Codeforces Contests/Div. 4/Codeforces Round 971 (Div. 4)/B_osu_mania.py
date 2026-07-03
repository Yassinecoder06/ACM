t = int(input())

for _ in range(t):
    n = int(input())

    indexes = []

    for _ in range(n):
        l = list(input())
        i = l.index('#')

        indexes.append(str(i+1))

    print(' '.join(indexes[::-1]))