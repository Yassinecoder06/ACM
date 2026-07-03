t = int(input())

for _ in range(t):
    n, k = map(int,input().split())
    
    if (n%2==1 and k%2==0) or k > n:
        print('NO')
        continue

    output = []

    if k * 1 <= n and not output:
        output = [1] * k
        s = n - k
        if s%2==0:
            output[0] += s
        else:
            output = []

    if k * 2 <= n and not output:
        output = [2]*k
        s = n - 2*k
        if s%2==0:
            output[0] += s
        else:
            output = []

    if output:
        print('YES')
        output = map(str, output)
        print(' '.join(output))
    else:
        print('NO')