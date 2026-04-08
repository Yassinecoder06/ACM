from collections import defaultdict

t = int(input())
for _ in range(t):
    n ,q= map(int, input().split())
    c = list(map(int, input().split()))
    s = defaultdict(int)
    for i in range(q):
        a = list(map(int, input().split()))
        if a[0] == 1:
            players = a[1]
            server = a[2]
            for i in range(server-1, n):
                if players > c[i] - s[i]:
                    players -= (c[i] - s[i])
                    s[i] = c[i]
                    
                else:
                    s[i] += players
                    players = 0
        else:
            print(s[a[1]-1])
        
                
                

