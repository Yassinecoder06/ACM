t = int(input())

def rotate_90(matrice):
    return [list(row) for row in zip(*matrice[::-1])]

def rotate_180(matrice):
    return [row[::-1] for row in matrice[::-1]]

def rotate_270(matrice):
    return rotate_180(rotate_90(matrice))

for _ in range(t):
    n = int(input())

    matrice = []
    for _ in range(n):
        matrice.append(list(input()))

    m1 = rotate_90(matrice)
    m2 = rotate_180(matrice)
    m3 = rotate_270(matrice)

    ans = 0
    for i in range((n + 1) // 2):
        for j in range(n // 2):
            cells = [
                matrice[i][j],
                m1[i][j],
                m2[i][j],
                m3[i][j]
            ]
            ones = cells.count('1')
            zeros = cells.count('0')
            ans += min(ones, zeros)
    print(ans) 