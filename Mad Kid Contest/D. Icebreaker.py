t = int(input())
for _ in range(t):
    n = int(input())
    l = len(str(n))
    if  n == int('9' * l):
        print((l-1)*9 + 9)
    elif  n >= int('8' * l):
        print((l-1)*9 + 8)
    elif  n >= int('7' * l):
        print((l-1)*9 + 7)
    elif  n >= int('6' * l):
        print((l-1)*9 + 6)
    elif  n >= int('5' * l):
        print((l-1)*9 + 5)
    elif  n >= int('4' * l):
        print((l-1)*9 + 4)
    elif  n >= int('3' * l):
        print((l-1)*9 + 3)
    elif  n >= int('2' * l):
        print((l-1)*9 + 2)
    elif  n >= int('1' * l):
        print((l-1)*9 + 1)
    else:
        print((l-1)*9)