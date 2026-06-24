from math import floor

t = int(input())

output = []

for _ in range(t):
    a, b, x = map(int, input().split())
    states_a = []
    curr, ops = a, 0
    states_a.append((curr, ops))
    while curr > 0:
        curr //= x
        ops += 1
        states_a.append((curr, ops))
        
    states_b = []
    curr, ops = b, 0
    states_b.append((curr, ops))
    while curr > 0:
        curr //= x
        ops += 1
        states_b.append((curr, ops))


    min_ops = float('inf')
    for val_a, ops_a in states_a:
        for val_b, ops_b in states_b:
            cost = ops_a + ops_b + abs(val_a - val_b)
            if cost < min_ops:
                min_ops = cost
                    
    output.append(str(min_ops))

print('\n'.join(output))