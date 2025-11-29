from math import gcd

n = int(input())
a = list(map(int, input().split()))

a.sort()
result = a[0]
for i in range(1,n):
    if gcd(a[i], result) != 1:
        result = gcd(a[i], result)
    else:
        result = 1
        break

print(1)
print(result)
    

