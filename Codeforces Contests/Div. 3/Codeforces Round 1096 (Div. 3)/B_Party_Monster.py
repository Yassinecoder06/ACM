t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    c1 = s.count("(")
    c2 = s.count(")")

    if c1 == c2:
        print("YES")
    else:
        print("NO")