t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    ok = False
    if y == 0 and x%3==0:
        ok = True
    elif y < 0 and -4*y <= x and (x-4*(-y))%3==0:
        ok = True
    elif y > 0 and x>= 2*y and (x-2*y)%3==0:
        ok = True

    if ok: 
        print("YES")
    else:
        print("NO")
        
        