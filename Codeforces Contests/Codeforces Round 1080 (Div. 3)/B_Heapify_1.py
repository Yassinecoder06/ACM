
t = int(input())

def odd_part(x: int) -> int:
    while x % 2 == 0:
        x //= 2
    return x

for _ in  range(t):
    n = int(input())
    a = list(map(int, input().split()))

    yes = True

    for i, val in enumerate(a, start=1):
        if odd_part(i) != odd_part(val):
            yes = False
            break
        
    
    print("YES") if yes else print("NO")
        