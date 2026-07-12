t = int(input())

for _ in range(t):
    n,m = map(int, input().split())

    arr = []

    for _ in range(n):
        a = list(map(int, input().split()))
        arr.append((a, sum(a)))

    result = [element for row in sorted(arr, key=lambda y:y[1], reverse=True) for element in row[0]]

    prefix_sum = [0] * (n*m+1)
    for i in range(1, n*m+1):
        prefix_sum[i] = prefix_sum[i-1] + result[i-1]

    print(sum(prefix_sum))