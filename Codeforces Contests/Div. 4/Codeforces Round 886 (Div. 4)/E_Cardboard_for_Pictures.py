t = int(input())

for _ in range(t):
    n, c = map(int, input().split())
    s = list(map(int, input().split()))

    x = 0
    y = 0
    for i in range(n):
        x += s[i]**2
        y += s[i]

    low = 1
    high = 10**18
    ans = 0
    while low < high:
        mid = (low+high)//2

        if mid *(n*mid+2*y) < c-x:
            low = mid +1
        else:
            ans = mid
            high = mid-1

    print(ans//2)