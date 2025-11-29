t = int(input())
for _ in range(t):
    s = list(input())
    digits = sorted(map(int, s))  # trie les chiffres par ordre croissant
    res = []
    for i in range(10):
        needed = 9 - i
        for j in range(len(digits)):
            if digits[j] >= needed:
                res.append(str(digits[j]))
                digits.pop(j)
                break
    print("".join(res))
