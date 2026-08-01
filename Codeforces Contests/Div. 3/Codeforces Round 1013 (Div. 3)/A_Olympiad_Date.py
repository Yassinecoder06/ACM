t = int(input())

for _ in range(t):
    target = {0: 3, 3:1, 1:1, 2:2, 5:1}
    n = int(input())
    a = list(map(int, input().split()))

    count = 0
    for i in range(n):
        if target.get(a[i],0):
            target[a[i]] -= 1
    
            if target[a[i]] == 0:
                del target[a[i]]    

        count += 1
    
        if not target:
            break

    if not target:
        print(count)
    else:
        print(0)