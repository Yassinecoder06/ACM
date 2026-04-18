from math import lcm
t = int(input())

for _ in range(t):
    a,b,c,m = map(int,input().split())
    count_abc = m // lcm(a, b, c)
    count_ab = m // lcm(a, b)
    count_bc = m // lcm(b, c)
    count_ca = m // lcm(c, a)
    count_a = m // a
    count_b = m // b
    count_c = m // c

    only_abc = count_abc
    only_ab = count_ab - only_abc
    only_bc = count_bc - only_abc
    only_ca = count_ca - only_abc
    
    only_a = count_a - (only_ab + only_ca + only_abc)
    only_b = count_b - (only_ab + only_bc + only_abc)
    only_c = count_c - (only_bc + only_ca + only_abc)

    res_a = (2 * only_abc) + (3 * only_ab) + (3 * only_ca) + (6 * only_a)
    res_b = (2 * only_abc) + (3 * only_ab) + (3 * only_bc) + (6 * only_b)
    res_c = (2 * only_abc) + (3 * only_bc) + (3 * only_ca) + (6 * only_c)

    print(res_a, res_b, res_c)










    


    