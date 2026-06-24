from collections import Counter
t = int(input())

for _ in range(t):
    n = int(input())
    strings = []

    for i in range(n):
        strings.append(input())

    strings= Counter(strings)
    arr = list(strings)

    count = 0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if (arr[i][0] == arr[j][0] and arr[i][1] != arr[j][1]) or (arr[i][1] == arr[j][1] and arr[i][0] != arr[j][0]):
                count += (strings[arr[i]]* strings[arr[j]])

    print(count)
