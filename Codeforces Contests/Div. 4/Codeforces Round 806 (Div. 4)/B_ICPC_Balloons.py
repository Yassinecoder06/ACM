from collections import defaultdict
t = int(input())

for _ in range(t):
    n = int(input())
    s = list(input())

    occ = defaultdict(int)
    result = 0

    for i in range(n):
        if occ[s[i]] == 0:
            occ[s[i]] += 1
            result += 2
            continue
        result += 1

    print(result)