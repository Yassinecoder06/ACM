t = int(input())
for _ in range(t):
    n = int(input())
    pair = []
    impair = []
    for i in range(1,n+1):
        if i%2 == 0: pair.append(str(i))
        else: impair.append(str(i))
    
    pair.extend(impair[::-1])
    print(" ".join(pair))
