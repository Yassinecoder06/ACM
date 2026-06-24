import sys

input = sys.stdin.read
data = input().split()

index = 0
t = int(data[index])
index += 1

for _ in range(t):
    n = int(data[index])
    index += 1
    p = [int(x) for x in data[index:index + n]]
    index += n
    
    ideal = list(range(n, 0, -1))
    i = 0
    while i < n and p[i] == ideal[i]:
        i += 1
    if i < n:
        target = ideal[i]
        j = p.index(target)
        p[i:j+1] = p[i:j+1][::-1]
    
    print(*p)
