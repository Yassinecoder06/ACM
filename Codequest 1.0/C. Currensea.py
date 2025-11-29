t = int(input())
results = []
for _ in range(t):
    n = int(input())
    possible = False
    for y in range(0, 10000):  
        if n - 111 * y < 0:
            break
        if (n - 111 * y) % 11 == 0:
            possible = True
            break
    results.append("YES" if possible else "NO")

print("\n".join(results))