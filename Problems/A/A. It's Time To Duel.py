t = int(input())
for _ in range(t):
    n = int(input()) 
    a = list(map(int, input().split()))
    max_wins_possible = n - 1
    ok = False
    if sum(a) > max_wins_possible:
        ok = True

    for i in range(0,n-1):
        if a[i] + a[i + 1] < 1:
            ok = True
            break

    print("YES") if ok else print("NO")

