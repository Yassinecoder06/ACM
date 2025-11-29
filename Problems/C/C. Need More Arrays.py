t = int(input())
results = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    new_array = [a[0]]
    k = 0
    for i in range(n):
        if new_array[k] + 1 < a[i]:
            new_array.append(a[i])
            k += 1

    results.append(str(len(new_array)))


print("\n".join(results))
#Accepted