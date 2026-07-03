t = int(input())

for _ in range(t):
    n = int(input())
    round_numbers = []
    
    power = 0
    temp_n = n
    while temp_n > 0:
        digit = temp_n % 10
        if digit != 0:
            round_numbers.append(digit * (10 ** power))
        temp_n //= 10
        power += 1
    
    print(len(round_numbers))
    print(*(round_numbers))
