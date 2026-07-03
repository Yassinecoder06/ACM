from collections import Counter
t = int(input())

for _ in range(t):
    n = int(input())

    counter = []
    triangle = False
    for i in range(n):
        x = list(input())
        cnt = Counter(x)
        
        if cnt.get('1', 0):
            if counter:
                x = cnt['1']
                if x!= counter[-1]:
                    triangle = True
            counter.append(cnt['1'])

    print('TRIANGLE') if triangle else print('SQUARE')