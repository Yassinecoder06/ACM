t = int(input())
for _ in range(t):
    n,a,b,c = map(int, input().split())

    days = 3*(n // (a+b+c))
    rest = n % (a+b+c)

    if rest != 0:
        if rest <= a:
            days +=1
        elif rest <= a+b:
            days += 2
        elif rest <= a+b+c:
            days += 3

    print(days)