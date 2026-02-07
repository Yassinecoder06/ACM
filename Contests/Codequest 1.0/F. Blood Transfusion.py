t = int(input())
for _ in range(t):
    n = int(input())
    injured = list(input().split())
    donors = list(input().split())
    donors_occ = {"A":0, "B":0, "AB": 0, "O": 0}
    injured_occ = donors_occ.copy()
    for i in range(n):
        donors_occ[donors[i]] += 1
        injured_occ[injured[i]] += 1


    map_blood = {0: "A", 1: "B", 2: "AB", 3: "O"}

    #every blood type donates to the same type of injured
    for i in range(4):
        if injured_occ[map_blood[i]] >= donors_occ[map_blood[i]]:
            injured_occ[map_blood[i]] -= donors_occ[map_blood[i]]
            donors_occ[map_blood[i]] = 0
        else:
            donors_occ[map_blood[i]] -= injured_occ[map_blood[i]]
            injured_occ[map_blood[i]] = 0
    
    if injured_occ["O"] > 0:
        print("NO")
    elif injured_occ["A"] + injured_occ["B"] - donors_occ["O"] > 0:
        print("NO")
    elif injured_occ["AB"] - donors_occ["A"] - donors_occ["B"] - donors_occ["O"] > 0 :
        print("NO")
    else:
        print("YES")
        

    