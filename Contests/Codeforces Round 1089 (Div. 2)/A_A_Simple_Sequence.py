t = int(input())
for _ in range(t):
    n = int(input())
    print(" ".join([str(i) for i in range(1,n+1)][::-1]))