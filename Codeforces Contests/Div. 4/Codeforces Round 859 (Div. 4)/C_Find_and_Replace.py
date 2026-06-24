from collections import defaultdict
t  = int(input())

for _ in range(t):
    n = int(input())
    s =  input()
    mapp = defaultdict(list)
    ok = True
    for i in range(n):
        if mapp[s[i]]:
            x = i - mapp[s[i]][-1]
            if x%2==1:
                ok = False
                break
        mapp[s[i]].append(i)

    if ok:
        print('YES')
    else:
        print('NO')