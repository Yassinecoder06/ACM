from collections import defaultdict
t = int(input())

for _ in range(t):
    n = int(input())
    output = ['0']*n
    strings = []
    d = defaultdict(int)
    for _ in range(n):
        strings.append(input())
        d[strings[-1]] = 1

    for i in range(n):
        s = strings[i]

        for j in range(1,len(s)):
            if d[s[:j]] == 1 and d[s[j:]] == 1:
                output[i] = '1'
                break

    print(''.join(output))