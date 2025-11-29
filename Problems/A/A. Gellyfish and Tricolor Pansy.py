t = int(input())
for _ in range(t):
    a,b,c,d = map(int, input().split())
    gelly = min(a,c)
    flower = min(b,d)
    if gelly - flower >= 0:
        print("Gellyfish")
    else:
        print("Flower")
#Accepted