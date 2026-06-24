t = int(input())

for _ in range(t):
    n = int(input())
    a = list(input())

    results = []
    result = 0
    for i in range(n):
        if a[i] == 'L':
            result += i
        else:
            result += n-i-1

    
    count = 0
    while count < n//2:
        if a[count] == 'L' and a[n-count-1] == 'R':
            a[count] = 'R'
            result += n-2*count-1
            results.append(result)
        elif a[count] == 'L' and a[n-count-1] == 'L':
            a[count] = 'R'
            result += n-2*count-1
            results.append(result)
            count += 1
        elif a[count] == 'R' and a[n-count-1] == 'R':
            a[n-count-1] = 'L'
            result += n-2*count-1
            results.append(result)
            count += 1
        else: 
            count += 1

    for _ in range(n-len(results)):
        results.append(result)    

    results = map(str, results)
    print(' '.join(results))  

