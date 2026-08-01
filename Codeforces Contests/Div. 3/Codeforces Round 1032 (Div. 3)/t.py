x = [i for i in range(40, 0, -1)]
print(x)

op = 0

for i in range(40):
    for j in range(i,40):
        if x[i] > x[j]:
            x[i], x[j] = x[j], x[i]
            op += 1

print(x)
print(op)    
