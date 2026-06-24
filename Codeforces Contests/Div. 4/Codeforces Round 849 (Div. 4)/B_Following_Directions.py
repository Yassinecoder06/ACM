t = int(input())

for _ in range(t):
    n = int(input())

    s= list(input())

    target = [0,0]
    ok = False
    for i in range(n):
        if s[i] == 'U':
            target[1] += 1
        elif s[i] == 'D':
            target[1] -= 1
        elif s[i] == 'R':
            target[0] += 1
        elif s[i] == 'L':
            target[0] -= 1

        if target == [1,1]:
            ok = True
            break
    if ok:
        print('YES')
    else:
        print('NO')