t = int(input())
for _ in range(t):
    n,m,k = map(int, input().split())

    if m <= n*k:
        print("No")
    else:
        print("Yes")