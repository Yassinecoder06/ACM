t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    output = 0
    a.sort()
    for i in range(1,n):
        if not a[i] == a[i-1] + 1 and a[i] < k:
            output += 1
        elif a[i] == k:
            output +=1
        
    print(output)