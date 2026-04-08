from math import ceil

# Input
recipe = input().strip()
nb, ns, nc = map(int, input().split())
pb, ps, pc = map(int, input().split())
r = int(input())

freq = {"B": recipe.count("B"), "S": recipe.count("S"), "C": recipe.count("C")}

def can_make(x):
    need_b = max(0, freq["B"] * x - nb)
    need_s = max(0, freq["S"] * x - ns)
    need_c = max(0, freq["C"] * x - nc)
    total_cost = need_b * pb + need_s * ps + need_c * pc
    return total_cost <= r

low, high = 0, 10**13  
while low < high:
    mid = (low + high + 1) // 2  
    if can_make(mid):
        low = mid
    else:
        high = mid - 1

print(low)
