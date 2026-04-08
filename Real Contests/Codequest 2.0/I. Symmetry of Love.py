n = int(input())
s = input()
m = int(input())

def humming_distance(ch1, ch2):
    d = abs(ord(ch1) - ord(ch2))
    return min(d, 26 - d)

def deletion_cost(s, k):
    cost = 0
    l, r = 0, len(s)-1
    while l < r:
        if l == k:
            l += 1
            continue
        if r == k:
            r -= 1
            continue
        cost += humming_distance(s[l], s[r])
        l += 1
        r -= 1
    return cost

results = [deletion_cost(s,-1)]

for k in range(n):
    cost = deletion_cost(s, k) + m
    results.append(cost)

print(min(results))