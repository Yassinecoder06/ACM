from collections import Counter, defaultdict

t = int(input())

for _ in range(t):
    g = defaultdict(int)
    for _ in range(3):
        x = list(input())
        cnt = Counter(x)
        for i in ['A', 'B', 'C']:
            g[i] += cnt[i]
    
    ans = sorted(g.items(), key=lambda x: x[1])

    print(ans[0][0])
