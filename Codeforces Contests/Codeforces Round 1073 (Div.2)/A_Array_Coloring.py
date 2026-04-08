t = int(input())

def solve(case: tuple, a: list):
    b = [case[i%2] for i in range(n)]

    indices = list(sorted(range(n), key= lambda i: a[i]))
    a = [a[i] for i in indices]
    b = [b[i] for i in indices]

    for i in range(n-1):
        if b[i] == b[i+1]:
            return False
    
    return True
    
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if solve((0, 1), a) or solve((1,0), a):
        print("YES")
    else:
        print("NO")
