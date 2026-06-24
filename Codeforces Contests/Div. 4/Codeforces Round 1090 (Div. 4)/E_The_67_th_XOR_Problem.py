t = int(input())

for _ in range(t):
    n = int(input())

    a = list(map(int, input().split()))
    max_xor = 0
    for i in range(n):
        for j in range(1+i, n):
            max_xor = max(max_xor, a[i]^a[j])

    print(max_xor)