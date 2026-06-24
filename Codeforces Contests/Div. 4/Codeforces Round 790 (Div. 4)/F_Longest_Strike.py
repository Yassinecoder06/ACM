from collections import Counter
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,k = map(int, input().split())

    a = list(map(int, input().split()))

    cnt = Counter(a)

    good = [x for x in cnt.keys() if cnt[x] >= k]

    good.sort()
    

    if not good:
        print(-1)
        continue

    best_l = best_r = good[0]
    l = r = good[0]

    for i in range(1, len(good)):
        if good[i] == good[i - 1] + 1:
            r = good[i]
        else:
            if r - l > best_r - best_l:
                best_l, best_r = l, r
            l = r = good[i]

    if r - l > best_r - best_l:
        best_l, best_r = l, r

    print(best_l, best_r)