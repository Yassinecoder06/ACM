t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    s =  input()
    occ = {"0":0,
           "1":0}
    for i in range(n):
        occ[s[i]] += 1
    max_k = occ["0"] // 2 + occ["1"] // 2
    min_k = abs(occ["0"] - occ["1"]) // 2
    if min_k <= k <= max_k and (k -(min_k)) % 2 == 0:
        print("YES")
    else:
        print("NO")
    
#Accepted