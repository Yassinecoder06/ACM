n = 6
l = []
for i in range(n):
    for j in range(i+1):
        l.append(2**i + 2**j)
print(l)