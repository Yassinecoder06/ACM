t = int(input())
results = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    b = [x % 2 for x in a]

    op1 = op2 = float('inf')

    if 0 in b:
        first_even = b.index(0)
        last_even = n - 1 - b[::-1].index(0)
        op1 = n - 1 - abs(first_even - last_even)

    if 1 in b:
        first_odd = b.index(1)
        last_odd = n - 1 - b[::-1].index(1)
        op2 = n - 1 - abs(first_odd - last_odd)

    op = min(op1, op2)

    results.append(str(op))

print("\n".join(results))

#Accepted