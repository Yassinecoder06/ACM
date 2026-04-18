t = int(input())

for _ in range(t):
    n,k = map(int, input().split())

    strips = [input().strip() for _ in range(k)]

    masks = [0] * n

    for i in range(n):
        mask = 0
        for j in range(k):
            mask |= 1 << (ord(strips[j][i]) -ord('a'))

        masks[i] = mask


    divisors = []
    for d in range(1, int(n**0.5) + 1):
        if n % d == 0:
            divisors.append(d)
            if d * d != n:
                divisors.append(n // d)


    divisors.sort()

    for d in divisors:
        ok = True
        group_letter = [''] * d

        for i in range(d):
            cur = (1 << 26) - 1

            j = i
            while j < n:
                cur &= masks[j]
                j += d

            if cur == 0:
                ok = False
                break

            letter_index = (cur & -cur).bit_length() - 1
            group_letter[i] = chr(letter_index+ord('a'))

        if ok:
            final = group_letter * (n//d)
            print("".join(final))
            break           