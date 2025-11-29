t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    a = [0]*n
    for i in range(n):
        if s[i] == ">":
            a[i] = 1
        elif s[i] == "<":
            a[i] = -1
    somme = 0

    if n == 1:
        if a[0] == 1:
            print("FAILURE")
        else:
            print("SUCCESS")
    else:
        if a[0] == 1 and a[-1] == -1:
            i = 0
            while i < n:
                somme += a[i]
                if somme == -1 and i != n - 1:
                    print("FAILURE")
                    break
                i += 1
            if somme > 0:
                print("FAILURE")
            elif somme == 0:
                print("SUCCESS")
            elif somme == -1 and  i == n:
                print("SUCCESS")
        else:
            print("FAILURE")

    """
    print("Test:")
    hits = 0
    direction = 1
    i = 0
    while True:
        if a[i] == 1 and direction == -1:
            a[i] = 0
            direction *= -1
            hits += 1

        elif a[i] == -1 and direction == 1:
            a[i] = 0
            direction *= -1
            hits += 1
        print(a, direction, hits)
        i += direction

        if i < 0 or i >= n:
            break
    
    if hits == n:
        print("SUCCESS")
    else:
        print("FAILURE")
    """



