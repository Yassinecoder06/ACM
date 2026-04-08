n = int(input())
a = list(map(int, input().split()))

a.sort()
out = sum(a)

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2  
    return True

for i in range(n-1, -1, -1):
    if a[i]%2 == 0:
        a[i] -= 2
        a[0] *= 2
        break

print(min(sum(a), out))

