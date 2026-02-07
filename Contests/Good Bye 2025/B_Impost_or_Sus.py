t = int(input())
for _ in range(t):
    w = list(input())
    r = 0
    n = len(w)

    if w[0] == "u":
        w[0] = "s"
        r+=1

    if w[n-1] == "u":
        w[n-1] = "s"
        r+=1

    for i in range(1,n-1):
        if w[i-1] == "s" and w[i] == "u" and w[i+1] == "u":
            w[i+1] = "s"
            r+=1
    print(r)
