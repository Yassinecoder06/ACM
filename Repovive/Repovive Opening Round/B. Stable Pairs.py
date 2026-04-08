t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if a[i] < a[j]:
                ok =True
                for element in a[i+1:j]:
                    if a[i] < element < a[j]:
                           ok = False
                           break
                if ok:    
                    count +=1
    print(count)
