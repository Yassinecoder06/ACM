n = int(input())
points = []
x_max = 0

for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
    x_max = max(x_max, x)

matrice = [[0] * (x_max + 3) for _ in range(3)]

row_map = {1: 0, 0: 1, -1: 2}

for x, y in points:
    matrice[row_map[y]][x] = 1

squares = 0

for i in range(x_max + 1):
    if matrice[0][i] == matrice[1][i] == 1 and matrice[0][i+1] == matrice[1][i+1] == 1:
        squares += 1

    if matrice[1][i] == matrice[2][i] == 1 and matrice[1][i+1] == matrice[2][i+1] == 1:
        squares += 1

    if matrice[0][i] == matrice[2][i] == 1 and matrice[0][i+2] == matrice[2][i+2] == 1:
        squares += 1
    
    if matrice[1][i] == 1 and matrice[0][i+1] == 1 and matrice[2][i+1] == 1 and matrice[1][i+2] == 1:
        squares += 1

print(squares)
