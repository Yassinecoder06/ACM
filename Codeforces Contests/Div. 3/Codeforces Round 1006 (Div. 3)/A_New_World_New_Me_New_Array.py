for _ in range(int(input())):
    n,k,p = map(abs, map(int, input().split()))
    print(-1) if n*p < k else print(k//p) if k%p==0 else print(k//p+1)