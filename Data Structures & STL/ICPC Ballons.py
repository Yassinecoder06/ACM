t = int(input())
f = []
for _ in range(t):
    n = int(input())
    ch = input()
    list = []
    ballons = 0
    for i in range(n):
        if ch[i] not in list:
            ballons += 2
            list.append(ch[i])
        else:
            ballons += 1
    f.append(ballons)

for j in range(t):
    print(f[j])



    
    
        
