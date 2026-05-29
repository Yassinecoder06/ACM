t = int(input())

for _ in range(t):
    n,m = map(int, input().split())
    a = list(map(int, input().split()))

    max_run = 1
    current_run = 1
    for i in range(n):
        if a[i] == a[i-1]:
            current_run += 1
        else:
            current_run = 1

        maw_run = max(max_run, current_run)

    if max_run >= m:
        print("YES")

    else:
        print("NO")