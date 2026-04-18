def mex(arr):
    s = 0
    while s in arr:
        s +=1

    return s

t = int(input())

for _ in range(t):
    n,k = map(int, input().split())

    a = set(map(int, input().split()))

    print(min(mex(a), k-1))



