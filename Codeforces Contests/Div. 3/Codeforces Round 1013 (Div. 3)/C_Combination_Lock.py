t = int(input())

for _ in range(t):
    n = int(input())

    if n % 2 == 0:
        print(-1)
        continue

    result = [str(n-i) for i in range(0,n-1)]
    result = ['1'] + result

    print(' '.join(result)) 