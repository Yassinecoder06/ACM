t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    k = arr[0]

    arr = list(map(lambda x: x - k, arr))
    arr.pop(0)
    if arr[0] >= k:
        k = arr[0]

    print(k)