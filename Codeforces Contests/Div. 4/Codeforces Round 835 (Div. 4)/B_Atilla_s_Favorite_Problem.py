t = int(input())

for _ in range(t):
    n = int(input())
    s = list(input())
    
    s.sort()
    print(ord(s[-1])-96)


    