t = int(input())
for _ in range(t):
    n,x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a = a[::-1]
    nb = 0
    i = 0
    counter = 1
    while i < n:
        if counter * a[i] >= x:
            nb += 1
            counter = 1
        else:
            counter += 1
        i += 1
    print(nb)

#Accepted