import sys

data = sys.stdin.read().split()
ptr = 0
t = int(data[ptr])
ptr += 1

results = []
for _ in range(t):
    n = int(data[ptr])
    ptr += 1
    a = list(map(int, data[ptr : ptr + n]))
    ptr += n
    
    pref1 = [0] * (n + 1)
    pref2 = [0] * (n + 1)
    pref3 = [0] * (n + 1)
    
    for i in range(n):
        pref1[i+1] = pref1[i] + (1 if a[i] == 1 else 0)
        pref2[i+1] = pref2[i] + (1 if a[i] == 2 else 0)
        pref3[i+1] = pref3[i] + (1 if a[i] == 3 else 0)
        
    f = [pref1[j] + pref2[j] - pref3[j] for j in range(n + 1)]
    
    s_max = [0] * (n + 1)
    s_max[n-1] = f[n-1]
    for j in range(n - 2, -1, -1):
        s_max[j] = max(f[j], s_max[j+1])
        
    found = False
    for i in range(1, n - 1):
        if pref1[i] >= (pref2[i] + pref3[i]):
            if i + 1 <= n - 1 and s_max[i+1] >= f[i]:
                found = True
                break
    
    results.append("YES" if found else "NO")
    
sys.stdout.write("\n".join(results) + "\n")
