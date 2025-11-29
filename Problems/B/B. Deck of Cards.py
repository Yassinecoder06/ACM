t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    L = s.count('0')
    R = s.count('1')
    F = s.count('2')

    L_min = L
    L_max = L + F
    R_min = R
    R_max = R + F

    result = []

    for i in range(1, n + 1):
        if i <= L_min or i > n - R_min:
            result.append('-')        # definitely removed
        elif i > L_max and i <= n - R_max:
            result.append('+')        # definitely remains
        else:
            result.append('?')        # unknown

    print("".join(result))
