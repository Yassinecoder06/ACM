t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int,input().split()))

    a.sort()
    b.sort()
    count = 0
    for x in b:
        if (x+count > len(a)):
            break
        arr = a[-(x + count):]
        a.remove(arr[0])
        count += (x-1)
    print(sum(a))