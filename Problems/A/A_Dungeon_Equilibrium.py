from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    a = map(int, input().split())
    c = Counter(a)
    deleting = 0
    for key, value in c.items():
        if value < key:
            deleting += value
        elif value > key:
            deleting += (value - key)
    print(deleting)