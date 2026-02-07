def who_wins(x1, y1, x2, y2, t):
    D = y1 - y2 - 1

    if x1 != x2:
        return "Ayumi" if t == 1 else "Mitsuhiko"
    else:
        parity = D % 2 
        if parity == 0:
            return "Ayumi" if t == 1 else "Mitsuhiko"
        else:
            return "Mitsuhiko" if t == 1 else "Ayumi"


x1, y1, x2, y2, t = map(int, input().split())
print(who_wins(x1, y1, x2, y2, t))
