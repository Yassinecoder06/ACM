print(4^11)

def int_to_bin(number):
    return list(format(number, '030b'))

def bin_to_int(string):
    return int(string, 2)

print(len(int_to_bin(292)))
print(bin_to_int("1010000101"))


def compare(number1, number2):
    x1 = int_to_bin(number1)
    x2 = int_to_bin(number2)
    result = ["0"]*30

    for i in range(30):
        if x1[i] == x2[i]:
            continue
        else:
            result[i] = "1"

    return bin_to_int("".join(result))



print(compare(998,244))