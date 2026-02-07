t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    key_count = {}
    r = 0
    for k in range(n):
        key = a[k] - k
        if key in key_count:
            r += key_count[key]  # Count pairs with the same key
            key_count[key] += 1
        else:
            key_count[key] = 1
    print(r)
