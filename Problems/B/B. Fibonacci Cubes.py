def f(i):
    if i == 1: return 1
    if i == 2: return 2
    return f(i - 1) + f(i - 2)

print(f(6))

t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    boxes = []
    for _ in range(m):
        w,l,h = map(int, input().split())
        boxes.append([w,l,h])
    
    cubes = [f(i) for i in range(1,n + 1)]
    result = ""
    
