n,k = map(int, input().split())
s = list(input())

alp = []
mapping = {}

for i in range(26):
    alp.append(chr(65+i))
    mapping[alp[i]] = i

alp = alp[:k]

x = 0
for i in range(1,n-1):
    if s[i] != s[i-1] and s[i] != s[i+1]:
        continue
    else:
        s[i] = s[(mapping[s[i-1]] + mapping[s[i+1]] + 1) % k]
        x += 1
        

