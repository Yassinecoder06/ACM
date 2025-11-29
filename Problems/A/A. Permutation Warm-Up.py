t = int(input())

def f(p):
    s = 0
    for i in range(len(p)):
        s += abs(p[i] - (i+1))
    return s

results = []
for _ in range(t):
    n = int(input())
    nums = [x for x in range(1,n+1)]
    reverse_nums = nums[::-1]
    mx = f(reverse_nums)
    results.append(str(mx // 2 + 1))

print("\n".join(results))

#Accepted