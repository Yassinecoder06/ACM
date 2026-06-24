t = int(input())

for _ in range(t):
    n = int(input())
    a = input()
    m = int(input())
    b = input()

    c = input()

    for i in range(len(c)):
        if c[i] == "V":
            a = b[i] + a
        elif c[i] == "D":
            a+= b[i]

    print(a)
