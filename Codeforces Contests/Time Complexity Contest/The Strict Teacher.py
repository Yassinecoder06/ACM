t = int(input())  # Number of test cases
results = []

for _ in range(t):
    n, m, q = map(int, input().split())
    b1, b2 = map(int, input().split())
    a = int(input())

    if b1 > b2:
        b1, b2 = b2, b1

    d1 = abs(a - b1)
    d2 = abs(a - b2)

    if b1 <= a <= b2:
        results.append((d1 + d2) // 2)
    else:
        if a > b2:
            results.append(min(d1, d2) + abs(n-a))
        elif a < b1:
            results.append(min(d1, d2) + abs(a-1))

for result in results:
    print(result)
        

    

    



