t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    even = a[0] % 2
    odd = a[1] % 2 
    ok = True
    for i in range(2,n):
        if i%2 == 1:
            if a[i]%2 != odd:
                ok = False
                break
        else:
            if a[i]%2 != even:
                ok = False
                break

    if ok:
        print('yes')
    else:
        print('no')