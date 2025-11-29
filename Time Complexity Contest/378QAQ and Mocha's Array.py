def is_beautiful_array(test_cases):
    results = []
    for n, a in test_cases:
        x = min(a)
        b = [y for y in a if y % x != 0]
        
        if not b:
            results.append("Yes")
        else:
            mb = min(b)
            if all(y % mb == 0 for y in b):
                results.append("Yes")
            else:
                results.append("No")
    return results

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

results = is_beautiful_array(test_cases)
print("\n".join(results))
