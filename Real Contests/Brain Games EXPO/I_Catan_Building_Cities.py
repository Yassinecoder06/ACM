n,k = map(int, input().split())

def check(nb, c, a, b, k):
    required_cards = 0
    for i in range(n):
        if nb > c[i]:
            required_cards += ((nb - c[i])*a[i] - b[i])
    return required_cards <= k
        
a = [0]*n
b = [0]*n
c = [0]*n
for i in range(n):
    a[i], b[i] = map(int, input().split())
    c[i] = b[i] // a[i]
    b[i] -= c[i] * a[i]
    
high = 2*10**9 + 1 
low = 0

while high > low:
    nb = (high+low + 1)//2
    if check(nb, c, a, b, k):
        low = nb
    else:
        high = nb - 1
        
print(low)
    