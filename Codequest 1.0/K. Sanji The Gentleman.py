n = int(input())
s = input()
bring = False
for i in range(n):
    if s[i] == "W":
        bring = True
        break

if bring:
    print("YES")
else:
    print("NO")