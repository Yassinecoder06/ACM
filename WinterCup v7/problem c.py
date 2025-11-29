import math

t = int(input())
def sum_coprime_products(n):
    total = 0
    for a in range(1, n):
        for b in range(a + 1, n + 1):
            if math.gcd(a, b) == 1:
                total += a * b
    return total * 2 + 1

for i in range(t):
    n = int(input())
    print(sum_coprime_products(n))
