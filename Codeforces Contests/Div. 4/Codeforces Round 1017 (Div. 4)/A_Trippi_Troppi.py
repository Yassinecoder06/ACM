t = int(input())

for _ in range(t):
    s = list(input().split())
    ans = ['']*3
    
    for i in range(3):
        ans[i] = s[i][0]
    
    print("".join(ans))