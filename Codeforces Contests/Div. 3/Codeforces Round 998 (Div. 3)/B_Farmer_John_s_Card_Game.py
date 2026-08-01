t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    rows = []
    for i in range(n):
        s = list(map(int, input().split()))
        s.sort()
        rows.append((s, i + 1))
    

    rows.sort()
    
    
    cards_played = []
    for j in range(m):
        for i in range(n):
            cards_played.append(rows[i][0][j])
            
   
    can = True
    for k in range(len(cards_played) - 1):
        if cards_played[k] > cards_played[k+1]:
            can = False
            break
            
    if can:
        ans = [str(rows[i][1]) for i in range(n)]
        print(' '.join(ans))
    else:
        print(-1)
