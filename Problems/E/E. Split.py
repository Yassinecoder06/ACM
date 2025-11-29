from collections import Counter
t = int(input())

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    if n % k != 0:
        return 0

    total_freq = Counter(a)
    count_awesome = 0

    for l in range(n):
        sub_freq = Counter()
        for r in range(l, n):
            sub_freq[a[r]] += 1

            ok = True
            for v in sub_freq:
                if sub_freq[v] * k > total_freq[v]:
                    ok = False
                    break

            if ok:
                count_awesome += 1

    return count_awesome


for _ in range(t):
    print(solve())
            
