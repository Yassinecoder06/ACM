import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    # 1) On cherche s_unique s’il y a au moins un b[i] != -1
    s_unique = None
    possible = True
    for ai, bi in zip(a, b):
        if bi != -1:
            si = ai + bi
            if s_unique is None:
                s_unique = si
            elif s_unique != si:
                possible = False
                break
    
    if not possible:
        print(0)
        continue
    
    # 2) Bornes de l’intersection ∩ [a[i], a[i]+k]
    L = max(a)
    R = min(ai + k for ai in a)
    
    # 3) Cas où s_unique est fixé ou libre
    if s_unique is not None:
        # s_unique doit tomber dans [L, R]
        print(1 if L <= s_unique <= R else 0)
    else:
        # tous les s ∈ [L, R] sont possibles
        print(max(0, R - L + 1))

#Accepted
