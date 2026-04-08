def draw(reverse, n):
    return ("##.." if reverse == 0 else "..##") * (n // 2) + ("##" if n % 2 and reverse == 0 else ".." if n % 2 else "")


t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(n):
        if i % 2 == 0:
            print(draw(0, n))
            print(draw(0, n))
        else:
            print(draw(1, n))
            print(draw(1, n))
