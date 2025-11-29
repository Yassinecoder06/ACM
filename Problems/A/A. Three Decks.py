t = int(input())
for _ in range(t):
    a,b,c = map(int, input().split())
    if (a+b+c) % 3 != 0: 
        print("NO")
    else:
        s = (a+b+c) // 3
        taken = c - s
        if b > s or a > s:
            print("NO")
        else:
            print("YES")
