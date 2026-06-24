from collections import Counter
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    cnt = Counter(a)

    ok = True
    for x in cnt:
        if cnt[x] > 1:
            ok = False
            break

    print('YES') if ok else print('NO')