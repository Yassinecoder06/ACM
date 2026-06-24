from math import log10, ceil

t = int(input())

for _ in range(t):
    n = int(input())

    results = []
    for k in range(1,ceil(log10(n))+1):
        if n%(1+10**k)==0:
            results.append(str(n//(1+10**k)))
    
    if not results:
        print(0)
    else:
        print(len(results[::-1]))
        print(" ".join(results[::-1]))