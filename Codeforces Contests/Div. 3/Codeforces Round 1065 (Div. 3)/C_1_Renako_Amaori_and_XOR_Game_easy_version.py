t = int(input())

for _ in range(t):
    n = int(input())

    a = list(map(str, input().split()))
    b = list(map(str, input().split()))

    bit_count_a = int("".join(a), 2).bit_count()
    bit_count_b = int("".join(b), 2).bit_count()
    #print(bit_count_a, bit_count_b)
    for i in range(n):
        if i % 2 == 0:
            if bit_count_a % 2 == 0:
                if a[i] == "0" and b[i] == "1":
                    a[i], b[i] = b[i], a[i]
                    bit_count_a += 1
                    bit_count_b -= 1

                elif a[i] == "1" and b[i] == "0":
                    a[i], b[i] = b[i], a[i]
                    bit_count_a -= 1
                    bit_count_b += 1
    
        else:
            if bit_count_b % 2 == 0:
                if a[i] == "1" and b[i] == "0":
                    a[i], b[i] = b[i], a[i]
                    bit_count_a -= 1
                    bit_count_b += 1

                elif a[i] == "0" and b[i] == "1":
                    a[i], b[i] = b[i], a[i]
                    bit_count_a += 1
                    bit_count_b -= 1
    
    bit_count_a %= 2
    bit_count_b %= 2

    if bit_count_a == bit_count_b:
        print("Tie")
    elif bit_count_a == 1:
        print("Ajisai")
    elif bit_count_b == 1:
        print("Mai")
