t = int(input())
out = []

for _ in range(t):
    n,k= map(int, input().split())
    s = input()
    
    ones_count = [0] * k
    
    for i in range(n):
        if s[i] == '1':
            ones_count[i % k] += 1
    
    possible = True
    for count in ones_count:
        if count % 2 != 0:
            possible = False
            break
    
    if possible:
        out.append("YES")
    else:
        out.append("NO")
        
print('\n'.join(out))