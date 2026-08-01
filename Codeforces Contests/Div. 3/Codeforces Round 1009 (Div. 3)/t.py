l = []

for i in range(31):
    for j in range(i, 31):
        y = (1 << i) | (1 << j)

        l.append(y)

l.sort()
print(l)