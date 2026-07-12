import sys

input_data = sys.stdin.read().split()

t = int(input_data[0])

results = []
idx = 1
for _ in range(t):
    n = int(input_data[idx])
    s = input_data[idx+1]
    idx += 2
    
    count_dash = s.count('-')
    count_underscore = s.count('_')
    
    if count_dash < 2 or count_underscore == 0:
        results.append("0")
        continue
    
    left_dashes = count_dash // 2
    right_dashes = count_dash - left_dashes
    
    ans = left_dashes * right_dashes * count_underscore
    results.append(str(ans))
    
print('\n'.join(results))

