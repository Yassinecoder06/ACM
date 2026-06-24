t = int(input())

for _ in range(t):
    n = int(input())
    s = list(input())
    prefix_distinct = [0] * n
    seen = set()
    for i in range(n):
        seen.add(s[i])
        prefix_distinct[i] = len(seen)
        
    suffix_distinct = [0] * n
    seen_right = set()
    for i in range(n - 1, -1, -1):
        seen_right.add(s[i])
        suffix_distinct[i] = len(seen_right)
        
    max_distinct = 0
    for i in range(n - 1):
        current_sum = prefix_distinct[i] + suffix_distinct[i + 1]
        if current_sum > max_distinct:
            max_distinct = current_sum
            
    print(max_distinct)

