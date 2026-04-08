n, q = map(int, input().split())
a = list(map(int, input().split()))

positions = {}
for i, val in enumerate(a, start=1):  
    if val not in positions:
        positions[val] = [i, i]  
    else:
        positions[val][1] = i

for _ in range(q):
    x = int(input())
    if x in positions:
        print(*positions[x])
    else:
        print("-1 -1")
