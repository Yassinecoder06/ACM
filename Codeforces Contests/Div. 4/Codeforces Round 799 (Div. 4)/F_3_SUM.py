from collections import Counter
t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x[-1]) for x in input().split()]
    counts = Counter(a)

    ok = False
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if (i + j + k) % 10 == 3:
                    req = Counter([i, j, k])
                    if all(counts[num] >= req[num] for num in req):
                        ok = True
                        break
            if ok:
                break
        if ok:
            break

    print("YES" if ok else "NO")
