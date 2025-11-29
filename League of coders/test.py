import itertools, random, subprocess, sys

# greedy algorithm (from your test.py)
def greedy(a):
    l=0; r=len(a)-1; mx=0; team=[]
    while l<=r:
        left=a[l]; right=a[r]
        if left<mx and right<mx:
            if l==r:
                l+=1
            else:
                l+=1; r-=1
        elif left>=mx and right>=mx:
            if left<=right:
                mx=left; team.append(left); l+=1
            else:
                mx=right; team.append(right); r-=1
        elif left>=mx:
            mx=left; team.append(left); l+=1
        else:
            mx=right; team.append(right); r-=1
    return sum(team), team

# brute force: try all valid sequences (choose end each step)
def brute(a):
    best_sum=-1; best_team=None
    n=len(a)
    for picks in range(1, 1<<n):
        # represent a sequence of choices L/R of length n, but we can stop earlier
        # Instead, enumerate all sequences of choices (L/R) up to length n
        pass
    # simpler brute: DFS enumerating all possible game plays
    from collections import deque
    best_sum=-1; best_team=[]
    def dfs(deq, mx, team):
        nonlocal best_sum, best_team
        if not deq:
            s=sum(team)
            if s>best_sum:
                best_sum=s; best_team=list(team)
            return
        # choose left
        x=deq[0]
        new=deque(deq)
        new.popleft()
        if x>=mx:
            dfs(new, x, team+[x])
        else:
            # discard not added
            dfs(new, mx, team)
        # choose right
        deq2=deque(deq)
        y=deq2.pop()
        if y>=mx:
            dfs(deq2, y, team+[y])
        else:
            dfs(deq2, mx, team)
    dfs(deque(a), 0, [])
    return best_sum, best_team

def find_counterexample(max_n=8, trials=10000, max_val=10):
    # try small exhaustive + random tests
    for n in range(1, max_n+1):
        for a in itertools.product(range(1, max_val+1), repeat=n):
            gsum, gteam = greedy(list(a))
            bsum, bteam = brute(list(a))
            if gsum != bsum:
                return a, gsum, gteam, bsum, bteam
    # random
    for _ in range(trials):
        n=random.randint(1, max_n)
        a=[random.randint(1, max_val) for _ in range(n)]
        gsum, gteam = greedy(list(a))
        bsum, bteam = brute(list(a))
        if gsum != bsum:
            return a, gsum, gteam, bsum, bteam
    return None

res = find_counterexample()
print(res)