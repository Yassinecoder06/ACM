t = int(input())
for _ in range(t):
    n,s,x = map(int, input().split())
    a = list(map(int, input().split()))
    k = sum(a)

    if k == s:
        print("YES")
    elif s < k:
        print("NO")
    else:
        if (s - k) % x == 0:
            print("YES")
        else:
            print("NO")
