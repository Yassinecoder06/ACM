n, t = map(int, input().split())
k = list(map(int, input().split()))

low, high = 1, 10**18 

def is_possible(time):
    products = 0
    for i in k:
        products += time // i
        if products >= t:  
            return True
    return False

while low < high:
    mid = (low + high) // 2
    if is_possible(mid):
        high = mid
    else:
        low = mid + 1

print(low)
