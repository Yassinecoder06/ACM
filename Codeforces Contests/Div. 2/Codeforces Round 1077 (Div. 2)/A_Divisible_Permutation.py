for _ in range(int(input())):
    n = int(input())
    p = [1, n]
    used = {1, n}
    for i in range(n - 2, 0, -1):
        prev = p[-1]
        if 1 <= prev - i <= n and prev - i not in used:
            p.append(prev - i)
            used.add(prev - i)
        else:
            p.append(prev + i)
            used.add(prev + i)
    p.reverse()
    print(*p)