from collections import Counter
t = int(input())

for _ in range(t):
    n = int(input())

    a= []
    b= []

    for _ in range(n):
        x,y = map(int, input().split())
        if y==0:
            a.append(x)
        else:
            b.append(x)

    cnta = Counter(a)
    cntb = Counter(b)

    result = 0
    for i in range(n+1):
        if cnta.get(i, False) and cntb.get(i, False):
            result += n-2

        if cntb.get(i, False):
            if cnta.get(i-1,False) and cnta.get(i+1,False):
                result += 1

        if cnta.get(i, False):
            if cntb.get(i-1,False) and cntb.get(i+1,False):
                result += 1

    print(result)