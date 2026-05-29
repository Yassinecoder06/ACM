t = int(input())


def get_prime_factors(n):
    factors = set()
    d = 2
    temp = n

    while d * d <= temp:
        while temp % d == 0:
            factors.add(d)
            temp //= d
        d += 1

    if temp > 1:
        factors.add(temp)
    return sorted(list(factors))

for _ in range(t):
    n = int(input())

    l = get_prime_factors(n)

    res = 1
    for i in l:
        res *= i

    print(res)


