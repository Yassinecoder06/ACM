from collections import Counter 
t = int(input()) 
for _ in range(t): 
    n,k = map(int, input().split()) 
    a = list(map(int, input().split())) 
    cnt = Counter(a) 
    v = cnt.get(a[0]) 
    c = False 
    for value in cnt.values(): 
        if value != v: 
            c = True 
    if c or v%k!=0: 
        print(0) 
        continue 
    v //= k 
    max_l = n // k 
    count = 0 
    
    for step in range(1,max_l+1): 
        for i in range(n): 
            if i+step>n: 
                break 
            ok = True 
            h = Counter(a[i:i+step]) 
            for value in h.values(): 
                if value > v: 
                    ok = False 
                    break 
            if ok: 
                count +=1 
    print(count) 