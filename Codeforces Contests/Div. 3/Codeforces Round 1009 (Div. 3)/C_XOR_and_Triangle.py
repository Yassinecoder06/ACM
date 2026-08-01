t = int(input())
for _ in range(t):
    x = int(input())
    ans = -1
    
    for i in range(31):
        for j in range(i, 31):
            y = (1 << i) | (1 << j)
            if y >= x:
                continue
            z = x ^ y
            if x + y > z and y + z > x and x + z > y:
                ans = y
                break
        if ans != -1:
            break
    print(ans)
