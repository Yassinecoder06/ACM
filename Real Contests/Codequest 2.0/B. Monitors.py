from math import sqrt, ceil

def can_power(moniters, batteries):
    delta = 9 + 4 * moniters
    a = ceil((-3 + sqrt(delta)) / 2)
    return moniters * a <= batteries

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    low, high = 1, n
    while low < high:
        mid = (low + high + 1) // 2 
        if can_power(mid, m):
            low = mid
        else:
            high = mid - 1
    print(low)
