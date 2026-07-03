t = int(input())

def get_groups(string):
    groups = []
    if not string: return groups
    char = string[0]
    count = 0
    for c in string:
        if c == char:
            count += 1
        else:
            groups.append((char, count))
            char = c
            count = 1
    groups.append((char, count))
    return groups

for _ in range(t):
    p = input()
    s = input()



    gp = get_groups(p)
    gs = get_groups(s)

    if len(gp) != len(gs):
        print('NO')
        continue

    possible = True
    for i in range(len(gp)):
        char_p, count_p = gp[i]
        char_s, count_s = gs[i]
        if char_p != char_s or not (count_p <= count_s <= 2 * count_p):
            possible = False
            break
    
    if possible:
        print('YES')
    else:
        print('NO')