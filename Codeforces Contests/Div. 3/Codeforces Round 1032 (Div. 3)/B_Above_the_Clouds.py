t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    if n < 3:
        print('No')
        continue

    cnt = {}
    cnt[s[0]] = 1
    cnt[s[-1]] = 1
    can = False
    for i in range(1,n-1):
        if cnt.get(s[i], False):
            can = True
            break
        else:
            cnt[s[i]] = 1

    print('Yes' if can else 'No')