a = list(map(int,input().split()))

a.sort()
r3 = a[3] - a[2]
r2 = a[2] - a[1]
r1 = a[1] - a[0]

if r3 == r2 == r1:
    r = r1
    if a[0] > r1:
        print(a[0]-r)

    else:
        print(a[3]+r)

elif r2 == r3:
    print(a[0]+r2)

elif r1 == r3:
    print(a[1] + r1)

elif r1 == r2:
    print(a[2] + r1)


