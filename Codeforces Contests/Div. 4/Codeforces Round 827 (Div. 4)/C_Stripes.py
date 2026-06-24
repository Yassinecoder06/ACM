import sys

input_data = sys.stdin.read().split()

t = int(input_data[0])
ptr = 1

for _ in range(t):
    grid = []
    for _ in range(8):
        grid.append(input_data[ptr])
        ptr += 1
    
    found_red = False
    for row in grid:
        if row == 'RRRRRRRR':
            found_red = True
            break
    
    if found_red:
        print('R')
    else:
        print('B')




    
