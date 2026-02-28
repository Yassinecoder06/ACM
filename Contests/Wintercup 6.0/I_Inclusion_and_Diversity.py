M=998244353 #is prime

m = int(input())

k = m // 2

factorial = [1] * (m+1)
inv_factorial = [1] * (m+1)

for i in range(1,m+1):
    factorial[i] = factorial[i-1] * i % M


inv_factorial[m] = pow(factorial[m], M-2, M)

for i in range(m, 0, -1):
    inv_factorial[i-1] = inv_factorial[i] * i % M

answer = (factorial[m] * inv_factorial[k] * inv_factorial[m-k]) % M

print(answer)

