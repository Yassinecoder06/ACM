import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    # Check if all equal:
    if min(a) == max(a):
        print("No")
        continue

    # Otherwise choose any a[k] > min(a):
    m = min(a)
    for k in range(n):
        if a[k] > m:
            idx = k
            break

    # Build answer:
    print("Yes")
    ans = ['2'] * n
    ans[idx] = '1'   # put a[idx] alone in B
    print(" ".join(ans))
