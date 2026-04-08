from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    a = deque(map(int, input().split()))

    mx = 0
    l = []

    while len(a) > 0:
        x = a[0]
        y = a[-1]

        if x < mx and y < mx:
            if len(a) == 1:
                a.popleft()
            else:
                a.popleft()
                a.pop()
        elif x >= mx and y >= mx:
            mx = min(x,y)
            if x < y:
                a.popleft()
            else:
                a.pop()
            l.append(str(mx))
        elif x >= mx:
            a.pop()
        elif y >= mx:
            a.popleft()


    print(len(l))
    print(" ".join(l))

