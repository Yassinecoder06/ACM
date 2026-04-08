t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    in_odd = False
    mx_odd = []
    result = 0
    for i in range(n):
        if a[i] % 2 == 1:
            mx_odd.append(a[i])
        else:
            result += a[i]

    if not mx_odd:
        print(0)
    else:
        mx_odd.sort()
        add = sum(mx_odd[len(mx_odd)//2:])
        print(result+add)
            
