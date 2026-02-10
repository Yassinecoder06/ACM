from collections import Counter
def solve():
    h,w = map(int,input().split())
    
    if h < 3 or w < 3:
        return False

    counter = 0
    matrice = []

    for i in range(h):
        row = list(input())
        for k in range(w):
            if row[k] == "*":
                counter += 1
                    
        matrice.append(row)

    rows = []
    if h%2==1:
        rows.append((h+1)//2 -1)
    else:
        rows.append(h//2 - 1)
        rows.append(h//2)
        
    columns = []
    if w%2==1:
        columns.append((w+1)//2 -1)
    else:
        columns.append(w//2-1)
        columns.append(w//2)
    x,y = locate(rows, columns, matrice)

    if x == -1 and y==-1:
        return False
    
    count = 0
    in_row = False
    in_col = False
    for i in range(w):
        if matrice[x][i] == "." and in_row:
            break
        elif matrice[x][i] == "*":
            in_row = True
            count += 1
    
    for j in range(h):
        if matrice[j][y] == "." and in_col:
            break
        elif matrice[j][y] == "*":
            in_col = True
            count += 1
    count-=1
            
    if count == counter:
        return True
    else:
        return False
        
def locate(rows, columns, matrice):
    for r in rows:
        for c in columns:
            if matrice[r][c] == '*' and matrice[r-1][c] == "*" and matrice[r+1][c] == "*" and matrice[r][c-1] == '*' and matrice[r][c+1] == '*':
                return r,c

    return -1, -1

if solve():
    print("YES")
else:
    print("NO")