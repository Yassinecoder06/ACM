t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    count_1_impair_a = 0
    count_1_pair_a = 0
    count_1_impair_b = 0
    count_1_pair_b = 0

    for i in range(n):
        if a[i] == b[i]:
            continue
        else:
            if i % 2 == 0:
                count_1_pair_a += a[i]
                count_1_pair_b += b[i]
            else:
                count_1_impair_a += a[i]
                count_1_impair_b += b[i]

    

        
