n,k = map(int, input().split())

def total_lines(v):
    total = 0
    current = v
    while current > 0:
        total += current
        current //= k
    return total

low, high = 1, n
while low < high:
    mid = (low + high) //2
    if total_lines(mid) >= n:
        high = mid
    else:
        low = mid + 1
    
print(low)