t = int(input())
for _ in range(t):
    n, m, l, r = map(int, input().split())
    k = n - m
    # nombre de pas vers la gauche qu'on utilise
    a = min(k, -l)
    # reconstitution de l'intervalle après m jours
    l_prime = l + a
    r_prime = l + m + a
    print(l_prime, r_prime)
