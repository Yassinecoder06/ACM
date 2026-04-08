n=int(input())
print(int(sum([-int(input()) for _ in range(n)])+n*(n+1)/2))
