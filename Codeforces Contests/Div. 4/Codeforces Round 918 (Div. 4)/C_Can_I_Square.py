import math

def is_perfect_square(n):
    if n < 0:
        return False  
    
    root = math.isqrt(n) 
    
    return root * root == n

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    s = sum(a)
    print('YES') if is_perfect_square(s) else print('NO')
