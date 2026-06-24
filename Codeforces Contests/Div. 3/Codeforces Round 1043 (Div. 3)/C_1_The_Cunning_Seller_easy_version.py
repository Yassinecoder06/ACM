from math import log,ceil

t = int(input())

for _ in range(t):
    n = int(input())
    
    c = 0
    for i in range(1, ceil(log(n,3))+1):
        if 3**i > n:
            break
        c += 1


    output = 0

    while n>0:
        q = (n // (3**c))
        n -= q * 3**c
        output += q * (3**(c+1) + c * 3**(c-1))

        c -= 1

    print(int(output))