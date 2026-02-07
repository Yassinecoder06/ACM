t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int,input().split()))
    p = [2**i for i in s]
    print(sum(p))