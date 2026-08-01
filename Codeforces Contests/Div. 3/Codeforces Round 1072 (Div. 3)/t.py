from math import ceil

div = {}       
def get_div_value(i):
    return i.bit_count() + i.bit_length() - 1

for i in range(1,100):
    div[i] = get_div_value(i)

print(div)

op = {}
for i in range(1,43):
    length = ceil((i+1)/2) 
    count = i - length
    number = int('1' + '0' * max(0,(length-count-1)) + '1' *count, 2)
    op[i] = [number, 2**(i-1)]


