t= int(input())

for _ in range(t):
    n = int(input())
    s = input()

    if len(set(s)) == 1:
        print(1)

    elif s == "".join(sorted(s)) or s == "".join(sorted(s, reverse=True)):
        print(2)
    else:
        print(1)