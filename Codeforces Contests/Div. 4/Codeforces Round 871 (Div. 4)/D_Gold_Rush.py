t = int(input())


def dp(s, m):
    if m > s:
        return False
    if s == m:
        return True
    
    elif s % 3 == 0:
        if s//3 == m or 2*s//3 == m:
            return True
        else: 
            return dp(s//3, m) or dp(2*s//3, m)
        
    return False

for _ in range(t):
    n,m = map(int, input().split())

    if dp(n,m):
        print('YES')
    else:
        print('NO')

    