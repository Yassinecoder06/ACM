from math import log, ceil

t = int(input())
for i in range(t):
    n = int(input())
    #the seller can sell 3**x for 3**(x+1) + x * 3**(x-1) = 3**(x-1) * (9 + x)
    x =  (n / log(3))
    price=3**(x-1)*(9+x)
    print(price)

