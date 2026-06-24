import sys


data = sys.stdin.read().split()
t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index]); index += 1
    h_list = list(map(int, data[index:index+n]))
    index += n
    
    m_val = min(h_list)
    k_min = (max(h_list) + 1) - m_val
    results.append(str(k_min))

print("\n".join(results))


