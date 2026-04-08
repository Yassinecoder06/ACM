q = int(input())
for _ in range(q):
    n = int(input())
    s,t = map(list, input().split())
    s.sort()
    t.sort()
    if s == t:
        print("YES")
    else:
        print("NO")