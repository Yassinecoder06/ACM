t = int(input())

for _ in range(t):
    k = int(input())

    c = list(map(int, input().split()))
    
    possible = False
    for x in c:
        if x >= 3:
            possible = True
            break
    
    if not possible:
        count_ge_2 = 0
        for x in c:
            if x >= 2:
                count_ge_2 += 1
        if count_ge_2 >= 2:
            possible = True
            
    print("YES" if possible else "NO")

