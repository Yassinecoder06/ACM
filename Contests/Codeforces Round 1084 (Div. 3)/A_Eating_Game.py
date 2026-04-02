from collections import Counter


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    cnt = Counter(a)

    print(cnt[max(a)])