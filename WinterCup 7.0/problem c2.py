MOD = 10**9 + 7
MAXN = 2 * 10**5 + 10  # marge de sécurité

# Étape 1 : Crible pour calculer phi[i] pour i de 1 à MAXN
phi = [0] * MAXN
for i in range(MAXN):
    phi[i] = i

for i in range(2, MAXN):
    if phi[i] == i:  # i est premier
        for j in range(i, MAXN, i):
            phi[j] -= phi[j] // i

# Étape 2 : Pré-calcul de la somme totale de brightness pour chaque n
brightness_sum = [0] * MAXN
for i in range(1, MAXN):
    # brightness(i) = (i^2 * phi(i)) // 2
    term = i * i % MOD
    term = term * phi[i] % MOD
    term = term * pow(2, MOD - 2, MOD) % MOD  # division par 2 modulo MOD
    brightness_sum[i] = (brightness_sum[i - 1] + term) % MOD

# Étape 3 : Lecture des entrées et réponses
t = int(input())
for _ in range(t):
    n = int(input())
    print(brightness_sum[n])
