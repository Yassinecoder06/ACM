t = int(input())

for _ in range(t):
    n = int(input())
    s = list(input())

    l = 0
    r = n-1

    while l < r:
        if s[l] == s[r]:
            break
        l+=1
        r-=1
    
    print(r-l+1)