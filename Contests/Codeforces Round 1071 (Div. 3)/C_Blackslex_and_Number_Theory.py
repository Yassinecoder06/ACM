def get_reachable(a, k, memo={}):
    """Get all values reachable from a using mod x where x >= k"""
    if (a, k) in memo:
        return memo[(a, k)]
    
    visited = {a}
    queue = [a]
    
    while queue:
        current = queue.pop(0)
        if current == 0:
            continue
        
        # Only need to try x up to current
        # since current % x = current for x > current
        for x in range(k, min(current + 1, k + 1000)):
            val = current % x
            if val not in visited:
                visited.add(val)
                queue.append(val)
    
    memo[(a, k)] = visited
    return visited

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    max_k = 0
    max_val = max(arr)
    
    # k can be at most around min(arr) in most cases
    # but to be safe, check values up to a reasonable limit
    for k in range(1, max_val + 1):
        # Get reachable sets for all elements
        reachable_sets = [get_reachable(a, k) for a in arr]
        
        # Find intersection of all reachable sets
        common = reachable_sets[0]
        for s in reachable_sets[1:]:
            common = common & s
        
        # If there's a common value, k is valid
        if common:
            max_k = k
    
    print(max_k)
