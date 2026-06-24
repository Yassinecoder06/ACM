high = 1000000
low = 1

while low < high:
    mid = (high + low + 1) // 2
    print(mid, flush=True)
    
    op = input()
    if op == '>=':
        low = mid       
    else:
        high = mid - 1  
print('!', low, flush=True)