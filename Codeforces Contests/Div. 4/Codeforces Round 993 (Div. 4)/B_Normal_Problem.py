t = int(input())

for _ in range(t):
    s = list(input())

    r = s[::-1]

    mapp = {"q":"p", "p":"q", "w":"w"}
    for i in range(len(r)):
        r[i] = mapp[r[i]]

    print("".join(r))
