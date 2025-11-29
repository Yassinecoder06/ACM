t = int(input())
results = []
for _ in range(t):
    x = int(input())
    a = [0, 0, 0]
    actions = 0
    ok = True
    while ok:
        for i in range(3):
            if sum(a) == 3 * x:
                ok = False
                break

            b = [a[j] for j in range(3)]
            b.pop(i)
            a[i] = min(b) * 2 + 1
            if a[i] > x:
                a[i] = x
            actions += 1

    results.append(str(actions))

print("\n".join(results))

#Accepted