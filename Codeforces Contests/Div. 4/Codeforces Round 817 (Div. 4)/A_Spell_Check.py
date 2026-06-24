t = int(input())

for _ in range(t):
    n = int(input())
    s = list(input())
    s.sort()

    target = list('Timur')
    target.sort()

    if n!=5:
        print('NO')
        continue
    
    if ''.join(s) == ''.join(target):
        print('YES')
    else:
        print('NO')


