import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, j, k = map(int, input().split())
    a = list(map(int, input().split()))
    strength = a[j-1]

    # Si k > 1, on peut s'arranger pour que j ne joue jamais → YES
    if k > 1:
        print("YES")
        continue

    # Sinon k == 1, j doit être max
    if strength == max(a):
        print("YES")
    else:
        print("NO")
