t = int(input())
for _ in range(t):
    n,x = map(int, input().split())
    a = list(map(int, input().split()))
    if 1 not in a:
        print("YES")
    else:
        first_1 = a.index(1)
        last_1 = (n -1) - a[::-1].index(1)
        if abs(last_1 - first_1 + 1) <= x:
            print("YES")
        else:
            print("NO")

#Accepted
