from collections import Counter
t = int(input())

for _ in range(t):
    s = input()
    cnt = Counter(s)
    result = sorted(cnt.items(), key=lambda x:x[1], reverse=True)
    print(result[0][0])