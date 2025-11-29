t = int(input())


def divisible_par5(binary):
    poids_mod5 = [1, 2, 4, 3]  # cycle de 2^i mod 5
    binary = binary[::-1]
    somme = 0

    for i, bit in enumerate(binary):
        somme += int(bit) * poids_mod5[i % 4]

    return somme % 5 == 0


def divisible_par7(binary):
    poids_mod7 = [1, 2, 4]  # cycle de 2^i mod 7
    binary = binary[::-1]
    somme = 0

    for i, bit in enumerate(binary):
        somme += int(bit) * poids_mod7[i % 3]

    return somme % 7 == 0


def divisible_par3(binary):
    binary = binary[::-1]
    s1 = 0
    s2 = 0

    for i, bit in enumerate(binary):
        if i % 2 == 0:
            s1 += int(bit)
        else:
            s2 += int(bit)

    return (s1 - s2) % 3 == 0


def divisible_par2(binary):
    return binary[-1] == '0'



