t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    a = []
    for char in s:
        if char in 'ae':
            a.append('V')
        else:
            a.append('C')

    res = []
    i = 0
    while i < n:
        if i + 2 >= n:
            res.append(s[i:])
            break
        
        if a[i+1] == 'V':
            if i + 2 < n and a[i+2] == 'C':
                if i + 3 < n and a[i+3] == 'V':
                    res.append(s[i:i+2])
                    i += 2
                else:
                    res.append(s[i:i+3])
                    i += 3
            else:
                res.append(s[i:i+2])
                i += 2
        else:
            res.append(s[i:i+3])
            i += 3

    print('.'.join(res))


    
