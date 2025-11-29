t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    s = '1'*k + '0'*(n-k)
    print(s)

#Accepted