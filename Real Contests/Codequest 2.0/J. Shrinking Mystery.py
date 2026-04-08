n,m = map(int, input().split())
all_drink_types = set([i for i in range(1,m+1)])

not_suspected = set()
suspected = all_drink_types.copy()
matrice = []
for _ in range(n):
    a = list(map(int, input().split()))
    k = a[0]
    drink_types = a[1:]
    matrice.append(drink_types)
s = input()

for i in range(n):
    if s[i] == "0":
        not_suspected.update(matrice[i])
    else:
        suspected.intersection_update(matrice[i])

all_drink_types.difference_update(not_suspected)

all_drink_types2 = [str(i) for i in all_drink_types]

if all_drink_types2:
    print(" ".join(all_drink_types2))
else:
    print(-1)