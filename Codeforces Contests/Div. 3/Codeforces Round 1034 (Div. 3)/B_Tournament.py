import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n, j, k = map(int, input().split())
    a = list(map(int, input().split()))
    strength = a[j-1]
 
    if k > 1:
        print("YES")
        continue
w 
    if strength == max(a):
        print("YES")
    else:
        print("NO")