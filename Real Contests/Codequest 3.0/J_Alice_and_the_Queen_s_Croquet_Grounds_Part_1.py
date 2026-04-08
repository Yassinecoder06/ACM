n = int(input())
r2 = 0

for _ in range(n):
    x,y = map(int,input().split())
    r2 = max(r2, x**2 + y**2)

print(r2)