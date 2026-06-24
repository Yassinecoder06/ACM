t = int(input())
for _ in range(t):
    matrice = []
    s= input()

    for _ in range(8):
        matrice.append(list(input()))

    row,col = 0,0
    for i in range(1,7):
        for j in range(1,7):
            if matrice[i][j] == '#':
                if matrice[i-1][j-1] == '#' and matrice[i+1][j+1] == '#' and matrice[i-1][j+1] == '#' and matrice[i+1][j-1] == '#':
                    row, col = i+1, j+1
                    break

        if row!=0 and col!=0:
            break
    print(row, col)