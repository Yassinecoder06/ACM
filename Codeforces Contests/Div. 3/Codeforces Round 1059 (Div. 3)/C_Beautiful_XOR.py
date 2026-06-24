t = int(input())

for _ in range(t):
    a,b = map(int, input().split())

    if a == b:
        print(0)
        continue

    x = a^b
    if x <= a:
        print(1)
        print(x)
        continue

    found = False

    for x1 in range(1, a+1):
        a_after = a ^ x1
        x2 = x1 ^ x
        if x2 <= a_after:
            print(2)
            print(x1, x2)
            found = True
            break

    if not found:
        print(-1)