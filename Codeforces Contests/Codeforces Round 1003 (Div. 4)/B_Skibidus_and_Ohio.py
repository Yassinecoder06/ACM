t = int(input())
for _ in range(t):
    s = input()
    ok = False
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            ok = True
    if ok: print(1)
    else:
        print(len(s))
