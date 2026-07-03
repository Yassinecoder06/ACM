from collections import Counter

for _ in range(int(input())):
    a = list(input())
    cnt = Counter(a)
    if len(cnt) == 1:
        print('NO')
    else:
        print('YES')
        for key in cnt.keys():
            if key != a[0]:
                index = a.index(key)
                a[0],a[index] = a[index],a[0]
                break

        print(''.join(a))