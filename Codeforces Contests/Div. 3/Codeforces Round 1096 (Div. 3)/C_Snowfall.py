t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    div6 = []
    div3 = []
    div2 = []
    els = []

    for i in range(n):
        if a[i] % 6 == 0:
            div6.append(a[i])
        elif a[i] % 2 == 0:
            div2.append(a[i])
        elif a[i] % 3 == 0:
            div3.append(a[i])
        else:
            els.append(a[i])

    print(" ".join(map(str, div6+div2+els+div3)))
        
             