t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    a = []
    for i in range(n):
        r = s[:i] if i > 0 else ""
        if s[i] == "1":
            r += "0"
        else:
            r+= "1"
        r += s[i+1:] if i < n else ""
        a.append(r)
    
    m = 0
    for i in range(n):
        ch = list(a[i])
        m += ch.count("1")
    
    print(m)
