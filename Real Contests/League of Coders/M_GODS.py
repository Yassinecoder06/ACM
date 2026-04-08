from math import log,ceil

t = int(input())

def to_base(base, number):
    if number == 0:
        return ["0"]
    seuil = ceil(log(number, base))
    s = []
    for i in range(seuil, -1, -1):
        q = number // base**i
        number -= (base**i * q)
        s.append(str(q))
    if s[0] == "0":
        return s[1:]
    return s

def to_alpha(array):
    s = ""
    for i in array:
        s+= chr(int(i)+ord("a"))
    return s

for _ in range(t):
    s, x =input().split()
    x = int(x)
    l = []
    for j in s:
        l.append(ord(j) - ord("a"))

    for i in range(2,x+1):
        g = []
        for j in l:
            g.extend(to_base(i,j))
        print(to_alpha(g))