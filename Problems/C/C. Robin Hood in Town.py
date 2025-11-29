t = int(input())

def unhappy(x, n, a):
    average_wealth = (sum(a) + x) / n
    number_of_unhappy = 0
    for i in  range(n):
        if a[i] < average_wealth / 2:
            number_of_unhappy += 1
    
    return number_of_unhappy > n / 2
    

def solve():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    low, high = 0, 4*10**11

    if len(a) == 2 or len(a) == 1:
        return -1
    
    while low < high:
        mid = (low + high - 1) // 2
        if unhappy(mid, n, a):
            high = mid 
        else:
            low = mid + 1

    return low


for _ in range(t):
    print(solve())

    
