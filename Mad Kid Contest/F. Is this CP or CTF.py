t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    decode = {
        "D": +1,
        "U": -1
    }

    for i in range(n):
        k, code = input().split()
        result = 0
        for c in code:                 
            result += decode[c]        
        a[i] = (a[i] + result) % 10     

    print(" ".join(map(str, a)))        
