from itertools import combinations

t = int(input())
for _ in range(t):
    n = int(input())

    count = 0
    for i in range(1,n):
        for j in range(1,n):
            if i == n - j:
                count += 1

    print(count)