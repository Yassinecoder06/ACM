from collections import Counter
t = int(input())

for _ in range(t):
    n,m = map(int, input().split())

    pos = [-1,-1]
    mx = 0
    for i in range(n):
        grid = list(input())

        try:
            index = grid.index('#')
        except:
            index = -1

        if index!=-1 and pos[1] == -1:
            cnt = Counter(grid)
            mx = cnt['#']
            pos[1] = index+1
            pos[0] = i+1
        elif index!=-1 and pos[1] != -1:   
            cnt = Counter(grid)

            if mx < cnt['#']:
                mx = cnt['#']
                pos[0] = i+1

    pos = list(map(str, pos))
    print(' '.join(pos))

        
