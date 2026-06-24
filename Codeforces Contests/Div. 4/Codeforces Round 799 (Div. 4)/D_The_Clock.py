t = int(input())

def compare(hour, minute):
    h = f"{hour:02d}"
    m = f"{minute:02d}"
    return h == m[::-1]

for _ in range(t):
    line = input().split()
    s = line[0]
    x = int(line[1])
    
    h, m = map(int, s.split(':'))
    start_time = h * 60 + m
    current_time = start_time
    
    seen_times = set()
    palindromes_seen = set()
    
    while current_time not in seen_times:
        seen_times.add(current_time)
        
        curr_h = current_time // 60
        curr_m = current_time % 60
        
        if compare(curr_h, curr_m):
            palindromes_seen.add(current_time)
            
        current_time = (current_time + x) % 1440
        
    print(len(palindromes_seen))