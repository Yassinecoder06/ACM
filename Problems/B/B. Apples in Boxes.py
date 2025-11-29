t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    t = 0
    if max(a) > 0: 
        a[a.index(max(a))] -= 1

    if (max(a) - min(a) > k):
        print("Jerry")
    else:
        s = sum(a)
        if s % 2 == 0:
            print("Tom")
        else:
            print("Jerry")

#Accepted
