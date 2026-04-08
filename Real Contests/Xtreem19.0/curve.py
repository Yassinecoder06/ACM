def modinv(a, p):
    return pow(a, p-2, p)  

def elliptic_add(P, Q, a, p):
    if P == None:
        return Q
    if Q == None:
        return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and (y1 + y2) % p == 0:
        return None  
    
    if x1 == x2 and y1 == y2:
        num = (3 * x1 * x1 + a) % p
        denom = (2 * y1) % p
    else:
        num = (y2 - y1) % p
        denom = (x2 - x1) % p

    lam = (num * modinv(denom, p)) % p
    x3 = (lam * lam - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p
    return (x3, y3)

T = int(input())
for _ in range(T):
    a, b, p, x1, y1, x2, y2 = map(int, input().split())
    P = (x1, y1)
    Q = (x2, y2)
    R = elliptic_add(P, Q, a, p)
    if R is None:
        print("POINT_AT_INFINITY")
    else:
        print(R[0], R[1])
