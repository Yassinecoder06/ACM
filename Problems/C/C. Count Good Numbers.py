def count_good(l, r):
    total = r - l + 1

    def cnt(k):
        return r // k - (l - 1) // k

    bad = (
        cnt(2) + cnt(3) + cnt(5) + cnt(7)
        - cnt(6) - cnt(10) - cnt(14) - cnt(15) - cnt(21) - cnt(35)
        + cnt(30) + cnt(42) + cnt(70) + cnt(105)
        - cnt(210)
    )

    return total - bad

t = int(input())
for _ in range(t):
    l,r = map(int, input().split())
    print(count_good(l,r))