t = int(input())

for _ in range(t):
    n = int(input())

    config = 0

    if n % 2 == 1 or  n==0:
        print(0)
    else:
        print(n//4+1)
