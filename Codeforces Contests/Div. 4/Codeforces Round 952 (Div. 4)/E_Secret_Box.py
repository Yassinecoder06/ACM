import sys

input_data = sys.stdin.read().split()

t = int(input_data[0])
ptr = 1

results = []
for _ in range(t):
    x = int(input_data[ptr])
    y = int(input_data[ptr+1])
    z = int(input_data[ptr+2])
    k = int(input_data[ptr+3])
    ptr += 4
    
    max_ways = 0
    
    for a in range(1, x + 1):
        if k % a == 0:
            k_div_a = k // a

            for b in range(1, y + 1):
                if k_div_a % b == 0:
                    c = k_div_a // b
                    if c <= z:
                        ways = (x - a + 1) * (y - b + 1) * (z - c + 1)
                        if ways > max_ways:
                            max_ways = ways
    
    results.append(str(max_ways))

sys.stdout.write('\n'.join(results) + '\n')
