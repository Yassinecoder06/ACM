from math import gcd

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    pgcd = a[0]

    for i in range(1,n):
        pgcd = gcd(pgcd, a[i])

    if pgcd == 1:
        return "2"

    for i in range(2, pgcd + 2):
        for j in range(n):
            if gcd(i, a[j]) == 1:
                return i

t = int(input()) 
for _ in range(t):
    print(main())
