n = 6
c = n * (n + 1) // 2
l = [0] * c
base = 1
for t in range(n):
    start_index = t * (t + 1) // 2
    l[start_index] = base + 1
    if t > 0:
        prev_start = (t - 1) * t // 2
        for j in range(1, t + 1):
            l[start_index + j] = 2 * l[prev_start + j - 1]
    base *= 2
print(l)