from collections import Counter
t = int(input())

for _ in range(t):
    s = list(input())
    k = list('codeforces')

    for i in range(10):
        s[i] = abs(ord(s[i]) - ord(k[i]))

    cnt = Counter(s)
    print(10-cnt[0])