t = int(input())
out = []

for i in range(1, t + 1):
    n = int(input())
    ans = []
    for j in range(n):
        ans.append(str(j + 1))
        ans.append(str(n + 1 + 2 * j))
        ans.append(str(n + 2 + 2 * j))
    out.append(" ".join(ans))
    
print("\n".join(out))