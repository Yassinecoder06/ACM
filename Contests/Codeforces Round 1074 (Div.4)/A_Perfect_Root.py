t = int(input())
for _ in range(t):
    n = int(input())
    output = []
    for i in range(n):
        output.append(str(i+1))
    print(" ".join(output))
