t = int(input())

def div2_counter(x):
    c = 0
    while x % 2 ==0:
        x //= 2
        c += 1
    return c

for _ in range(t):
    a,b = map(int, input().split())

    ans = -1

    if (a * b + 1) % 2 == 0:
        ans = max(ans, a * b + 1)

    if b % 2 == 0:
        val = (a * (b // 2)) + 2
        if val % 2 == 0:
            ans = max(ans, val)

    print(ans)
            
    
