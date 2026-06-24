t = int(input())

for _ in range(t):
    n = int(input())

    a = [0] * n
    for i in range(n):
        if i % 2 == 0:
            a[i] = -1
        else:
            if i == n - 1:
                a[i] = 2
            else:
                a[i] = 3
    
    print(*(map(str, a)))


        
        