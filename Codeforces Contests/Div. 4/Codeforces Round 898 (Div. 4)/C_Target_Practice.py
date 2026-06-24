import sys


input = sys.stdin.read
data = input().split()


t = int(data[0])
idx = 1

out = []
for _ in range(t):
    total_points = 0
    # Lire les 10 lignes de la grille actuelle
    for r in range(10):
        row = data[idx]
        idx += 1
        for c in range(10):
            if row[c] == 'X':
                # Calculer la valeur de l'anneau (basé sur 1)
                points = min(r, 9 - r, c, 9 - c) + 1
                total_points += points
    out.append(str(total_points))
    
print('\n'.join(out))


