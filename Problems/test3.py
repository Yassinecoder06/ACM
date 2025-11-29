n = int(input())
a = list(map(int, input().split()))

occ_succesive = {}
in_succ = False
for i in range(n):
    if str(a[i]) not in occ_succesive.keys():
        occ_succesive[str(a[i])] = 1
    else:
        if a[i] == a[i-1] and not in_succ:
            in_succ = True
            occ_succesive[str(a[i])] += 1
        elif a[i] == a[i-1] and in_succ:
            occ_succesive[str(a[i])] += 1
        else:
            in_succ = False

number_max_occ_succesive = int(max(occ_succesive, key = occ_succesive.get))
occ_succesive_max = occ_succesive[str(number_max_occ_succesive)]
number_min = min(a)
occ_succesive_min = occ_succesive[str(number_min)]
min_cost = min(number_max_occ_succesive*(n-occ_succesive_max),number_min*(n-occ_succesive_min))
print(min_cost)
