import sys

# Use generator to handle large inputs memory-efficiently
def input_gen():
    for line in sys.stdin:
        for token in line.split():
            yield token

def solve():
    tokens = input_gen()
    try:
        t_str = next(tokens)
    except StopIteration:
        return
        
    t = int(t_str)
    
    for _ in range(t):
        try:
            n = int(next(tokens))
            s = next(tokens)
        except StopIteration:
            break
            
        cnt_zeros = s.count('0')
        move_indices = []
        
        # First part should be all 0s. Collect indices of 1s in this range.
        for i in range(cnt_zeros):
            if s[i] == '1':
                move_indices.append(i + 1)
        
        # Second part should be all 1s. Collect indices of 0s in this range.
        for i in range(cnt_zeros, n):
            if s[i] == '0':
                move_indices.append(i + 1)
        
        if not move_indices:
            print("Bob")
        else:
            print("Alice")
            print(len(move_indices))
            # Use map and join to print space-separated integers
            print(" ".join(map(str, move_indices)))

if __name__ == '__main__':
    solve()    



