t = int(input())

for _ in range(t):
    n = int(input())
    colors = []
    mapp = {'R':'R','G':'G','B':'G'}
    for _ in range(2):
        s = list(input())

        for i in range(n):
            s[i] = mapp[s[i]]

        s = ''.join(s)
        colors.append(s)

    if colors[0] == colors[1]:
        print('YES')
    else:
        print('NO')