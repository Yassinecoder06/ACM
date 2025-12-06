from itertools import combinations

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    combs = list(combinations(arr, 7))
    print(len(combs))
    for c in combs:
        print(*c)