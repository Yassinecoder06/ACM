import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().strip()
    # scan prefixes up to the one-before-last character:
    bal = 0
    broken = False
    # we only care about prefixes ending at positions 0 .. len(s)-2
    for c in s[:-1]:
        bal += 1 if c == '(' else -1
        if bal == 0:
            print("YES")
            broken = True
            break
    if not broken:
        print("NO")

#Accepted